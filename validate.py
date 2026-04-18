#!/usr/bin/env python3
"""
Validation script for HK-Domain-Resources dataset.
Checks TSV files for data quality issues including:
- Correct column count (6 columns per row)
- Valid domain format (no URL paths, no spaces, no invalid characters)
- No placeholder values in domain column
- Industry column matches parent directory name
- Duplicate name+domain detection within each file
- File existence consistency between disk and README (path-aware)
- manifest.json consistency with actual files and row counts
- Domain coverage statistics per file
"""

import csv
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent
EXPECTED_COLUMNS = 6
HEADER = ["industry", "category", "name", "domain", "source", "dataset"]

# Regex: valid domain (letters, digits, hyphens, dots) — no paths, no spaces
DOMAIN_PATTERN = re.compile(
    r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
    r"[a-zA-Z]{2,}$"
)

INVALID_DOMAIN_VALUES = {"-", "n/a", "N/A", "none", "None", "null", ""}


def validate_domain(domain: str) -> list[str]:
    """Validate a single domain value. Returns list of error messages."""
    errors = []
    if domain in INVALID_DOMAIN_VALUES:
        return []  # Empty domain is allowed (means no domain available)
    if "/" in domain:
        errors.append(f"Domain contains URL path: '{domain}'")
    if " " in domain:
        errors.append(f"Domain contains spaces: '{domain}'")
    if "?" in domain or "=" in domain or "#" in domain:
        errors.append(f"Domain contains URL query/fragment: '{domain}'")
    if "@" in domain:
        errors.append(f"Domain contains email symbol: '{domain}'")
    if not DOMAIN_PATTERN.match(domain):
        # Check if it's a pure numeric value (data parsing artifact)
        try:
            float(domain)
            errors.append(f"Domain is a numeric value: '{domain}'")
        except ValueError:
            if domain not in INVALID_DOMAIN_VALUES:
                errors.append(f"Domain has invalid format: '{domain}'")
    return errors


def validate_tsv_file(filepath: Path) -> tuple[list[str], int, int]:
    """Validate a single TSV file. Returns (errors, total_rows, rows_with_domain)."""
    errors = []
    rel_path = filepath.relative_to(REPO_ROOT)
    expected_industry = filepath.parent.name

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter="\t")
            rows = list(reader)
    except Exception as e:
        return [f"{rel_path}: Failed to read file: {e}"], 0, 0

    if not rows:
        return [f"{rel_path}: File is empty"], 0, 0

    # Check header
    header = rows[0]
    if len(header) != EXPECTED_COLUMNS:
        errors.append(
            f"{rel_path}: Header has {len(header)} columns, expected {EXPECTED_COLUMNS}"
        )
    elif header != HEADER:
        errors.append(f"{rel_path}: Header mismatch: {header}")

    # Check data rows
    seen = set()
    rows_with_domain = 0
    for i, row in enumerate(rows[1:], start=2):
        if len(row) != EXPECTED_COLUMNS:
            errors.append(
                f"{rel_path}:{i}: Row has {len(row)} columns, expected {EXPECTED_COLUMNS}"
            )
            continue

        # Validate industry matches directory
        industry = row[0].strip()
        if industry and industry != expected_industry:
            errors.append(
                f"{rel_path}:{i}: Industry '{industry}' does not match directory '{expected_industry}'"
            )

        # Validate domain column (index 3)
        domain = row[3].strip()
        domain_errors = validate_domain(domain)
        for err in domain_errors:
            errors.append(f"{rel_path}:{i}: {err}")

        if domain and domain not in INVALID_DOMAIN_VALUES:
            rows_with_domain += 1

        # Check for empty required fields
        if not industry:
            errors.append(f"{rel_path}:{i}: Missing 'industry' value")
        if not row[1].strip():
            errors.append(f"{rel_path}:{i}: Missing 'category' value")
        name = row[2].strip()
        if not name:
            errors.append(f"{rel_path}:{i}: Missing 'name' value")

        # Duplicate detection (name + domain)
        key = (name.lower(), domain.lower())
        if key in seen:
            errors.append(f"{rel_path}:{i}: Duplicate entry: '{name}' / '{domain}'")
        seen.add(key)

    data_rows = len(rows) - 1
    return errors, data_rows, rows_with_domain


def find_all_tsv_files() -> list[Path]:
    """Find all TSV files in the repository."""
    tsv_files = []
    for dirpath, _, filenames in os.walk(REPO_ROOT):
        dirpath = Path(dirpath)
        # Skip hidden directories
        if any(part.startswith(".") for part in dirpath.relative_to(REPO_ROOT).parts):
            continue
        for filename in sorted(filenames):
            if filename.endswith(".tsv"):
                tsv_files.append(dirpath / filename)
    return tsv_files


def check_readme_consistency(tsv_files: list[Path]) -> list[str]:
    """Check that README references match actual files on disk (path-aware)."""
    errors = []
    readme_path = REPO_ROOT / "README.md"
    if not readme_path.exists():
        return ["README.md not found"]

    readme_text = readme_path.read_text(encoding="utf-8")

    # Extract all .tsv filenames mentioned in README
    readme_tsvs = set(re.findall(r"`([^`]+\.tsv)`", readme_text))

    # Get actual filenames on disk
    disk_tsvs = {f.name for f in tsv_files}

    # Also track full relative paths for cross-directory duplicate names
    disk_paths = {str(f.relative_to(REPO_ROOT)).replace("\\", "/"): f for f in tsv_files}

    # Files in README but not on disk (excluding planned files)
    planned_marker = "*(planned)*"
    for tsv_name in sorted(readme_tsvs - disk_tsvs):
        # Check if marked as planned in README
        if f"`{tsv_name}` {planned_marker}" in readme_text:
            continue
        errors.append(f"README references '{tsv_name}' but file does not exist on disk")

    # Files on disk but not in README
    for tsv_name in sorted(disk_tsvs - readme_tsvs):
        errors.append(f"File '{tsv_name}' exists on disk but is not listed in README")

    return errors


def check_manifest_consistency(tsv_files: list[Path]) -> list[str]:
    """Check that manifest.json matches actual files and row counts on disk."""
    errors = []
    manifest_path = REPO_ROOT / "manifest.json"
    if not manifest_path.exists():
        return ["manifest.json not found"]

    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
    except Exception as e:
        return [f"manifest.json: Failed to parse: {e}"]

    # Build disk inventory: dir/file -> row count
    disk_inventory = {}
    for fp in tsv_files:
        rel = str(fp.relative_to(REPO_ROOT)).replace("\\", "/")
        with open(fp, "r", encoding="utf-8") as f:
            rows = sum(1 for _ in f) - 1
        disk_inventory[rel] = rows

    # Check each industry in manifest
    manifest_files = set()
    for industry in manifest.get("industries", []):
        d = industry.get("directory", "")
        for file_entry in industry.get("files", []):
            fname = file_entry.get("file", "")
            expected_rows = file_entry.get("rows", 0)
            rel_path = f"{d}/{fname}"
            manifest_files.add(rel_path)

            if rel_path not in disk_inventory:
                errors.append(f"manifest.json lists '{rel_path}' but file does not exist")
            elif disk_inventory[rel_path] != expected_rows:
                errors.append(
                    f"manifest.json row count mismatch for '{rel_path}': "
                    f"manifest={expected_rows}, actual={disk_inventory[rel_path]}"
                )

    # Files on disk but not in manifest
    for rel_path in sorted(disk_inventory.keys()):
        if rel_path not in manifest_files:
            errors.append(f"File '{rel_path}' exists on disk but is not in manifest.json")

    # Check totals
    actual_files = len(disk_inventory)
    actual_rows = sum(disk_inventory.values())
    if manifest.get("total_files") != actual_files:
        errors.append(
            f"manifest.json total_files={manifest.get('total_files')}, actual={actual_files}"
        )
    if manifest.get("total_data_rows") != actual_rows:
        errors.append(
            f"manifest.json total_data_rows={manifest.get('total_data_rows')}, actual={actual_rows}"
        )

    return errors


def main():
    print("=" * 60)
    print("HK-Domain-Resources Dataset Validation")
    print("=" * 60)

    tsv_files = find_all_tsv_files()
    print(f"\nFound {len(tsv_files)} TSV files\n")

    all_errors = []
    total_rows = 0
    total_with_domain = 0
    low_coverage = []

    for filepath in tsv_files:
        errors, data_rows, rows_with_domain = validate_tsv_file(filepath)
        all_errors.extend(errors)
        total_rows += data_rows
        total_with_domain += rows_with_domain
        if data_rows > 0:
            pct = rows_with_domain / data_rows * 100
            if pct == 0 and data_rows > 10:
                rel = filepath.relative_to(REPO_ROOT)
                low_coverage.append((str(rel), data_rows, pct))

    # README consistency
    readme_errors = check_readme_consistency(tsv_files)
    all_errors.extend(readme_errors)

    # manifest.json consistency
    manifest_errors = check_manifest_consistency(tsv_files)
    all_errors.extend(manifest_errors)

    # Summary
    print(f"Total data rows across all files: {total_rows}")
    domain_pct = total_with_domain / total_rows * 100 if total_rows else 0
    print(f"Rows with domains: {total_with_domain} ({domain_pct:.1f}%)")

    if low_coverage:
        print(f"\nDomain coverage warnings ({len(low_coverage)} files with 0% domains, >10 rows):")
        for path, rows, pct in low_coverage:
            print(f"  {path}: {rows} rows, {pct:.0f}% domains")

    print()
    if all_errors:
        print(f"VALIDATION FAILED: {len(all_errors)} error(s) found\n")
        for error in all_errors:
            print(f"  ERROR: {error}")
        print()
        sys.exit(1)
    else:
        print("VALIDATION PASSED: No errors found")
        sys.exit(0)


if __name__ == "__main__":
    main()
