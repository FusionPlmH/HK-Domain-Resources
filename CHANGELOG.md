# Changelog

All notable changes to the HK-Domain-Resources dataset will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2026-Q2] - 2026-04-19

### Added (Phase 5 - Data Source Expansion & Missing Industries)
- **finance_insurance/tcsp_licensee.tsv** — 7,322 Trust & Company Service Provider licensees (from Companies Registry TCSP Register CSV)
- **finance_insurance/licensed_money_lender.tsv** — 1,949 licensed money lenders (from Companies Registry Money Lenders Register CSV)
- **construction/registered_electrical_contractor.tsv** — 14,607 EMSD registered electrical contractors (from EMSD open data XLSX)
- **healthcare_social/hospital.tsv** — 45 hospitals (31 HA public + 14 private, curated — HA API blocked)
- **accommodation_food/hotel.tsv** — 50 major licensed hotels
- **accommodation_food/restaurant_chain.tsv** — 30 major restaurant chains and F&B operators
- **agriculture_fishing/agriculture_fishing.tsv** — 12 agriculture & fishing entities (AFCD, farms, aquaculture)
- **mining_quarrying/mining_quarrying.tsv** — 5 mining & quarrying entities (CEDD, quarry operators)
- **scientific_technical/scientific_technical.tsv** — 33 scientific & technical services (HKSTP, R&D centres, testing labs, engineering, architecture, surveying)
- **information_communications/tech_company.tsv** — 33 HKSTP/Cyberport tech companies (fintech, biotech, AI, logistics tech)
- 3 new industry directories: `agriculture_fishing/`, `mining_quarrying/`, `scientific_technical/`

### Changed
- README: Updated industry count from 16 to 19 (added 3 new industries)
- README: Added new files under existing industries (hotels, restaurants, hospitals, EMSD contractors, TCSP, money lenders, tech companies)
- manifest.json: Updated with all new files and row counts (66 → 76 files, 7,178 → 31,264 rows)
- Fixed EMSD processing performance: switched from cell-by-cell to iter_rows() for 14K-row XLSX

## [2026-Q2] - 2026-04-18

### Fixed
- **pension_trustees.tsv**: Corrected 8 malformed domain values that contained URL paths instead of clean domains (e.g. `bocpt.com/homepage/en` → `bocpt.com`, `hk/en/index.html` → `aia.com.hk`)
- **ngo_hkcss_ctgoodjobs.tsv**: Removed invalid domain placeholders (`-` and `27.6`) for organizations without websites
- **banking_payments.tsv**: Cleaned 4 name fields that contained descriptions/emails/titles instead of organization names (e.g. Bank of China branch address → `Bank of China (Hong Kong) Limited`)
- **capital_markets.tsv** (public_administration): Removed misclassified "Council for the AIDS Trust Fund" (already correctly listed in `healthcare.tsv`)
- **pension_trustees.tsv** (public_administration): Replaced misclassified AIDS Trust Fund entry with correct MPFA entry
- **industry_association.tsv** (public_administration): Reclassified HKMA from `industry_association` to `regulators_statutory` category

### Added
- `validate.py` — automated validation script checking column counts, domain format, placeholder values, and README-disk consistency
- `.github/workflows/validate.yml` — GitHub Actions CI pipeline to run validation on push/PR
- `.gitignore` — excludes OS artifacts and temporary files
- `CHANGELOG.md` — version tracking for dataset changes
- `manifest.json` — machine-readable index of all TSV files with row counts and metadata
- README: Added missing education files (`education_ipass_associate_degree.tsv`, `education_ugc_funded_university.tsv`)
- README: Added missing public administration files (banking_payments, capital_markets, insurance, pension_trustees, industry_association, healthcare, environment, public-safety, social-welfare, tourism_tichk_travel_agent)
- README: Added quarterly update schedule (Jan, Apr, Jul, Oct)
- **finance_insurance/licensed_bank.tsv** — 148 HKMA-licensed banks (from HKMA Register of Authorized Institutions)
- **finance_insurance/restricted_licence_bank.tsv** — 16 restricted licence banks
- **finance_insurance/deposit_taking_company.tsv** — 11 deposit-taking companies
- **finance_insurance/sfc_licensed_corporation.tsv** — 46 SFC-licensed corporations (Types 1-9)
- **finance_insurance/virtual_asset_provider.tsv** — 10 licensed/deemed Virtual Asset Service Providers
- **finance_insurance/insurance_broker.tsv** — 15 major licensed insurance brokers
- **information_communications/telecom_licensee.tsv** — 28 OFCA-licensed telecom operators, ISPs, and broadcasters
- **professional_services/accounting_firm.tsv** — 14 HKICPA-registered CPA firms
- **professional_services/law_firm.tsv** — 28 Law Society-registered law firms
- **professional_services/management_consulting.tsv** — 8 management consulting firms
- **manufacturing/manufacturer.tsv** — 18 major HK manufacturers
- **utilities/electricity.tsv** — 2 electricity companies
- **utilities/gas.tsv** — 2 gas companies
- **utilities/water.tsv** — 1 water supply entity
- **utilities/waste_management.tsv** — 3 waste management companies
- **real_estate/property_developer.tsv** — 21 major property developers & REITs
- **construction/registered_contractor.tsv** — 16 construction & engineering contractors
- 6 new industry directories: `information_communications/`, `professional_services/`, `manufacturing/`, `utilities/`, `real_estate/`, `construction/`

### Changed
- README: Updated industry count from 11 to 16 (added 6 new industries)
- README: Marked 5 ORPHF healthcare files as *(planned)* since they don't yet exist on disk
- README: Updated "Last Updated" date to 2026-04-18

## [2026-Q1] - 2026-01-15

### Added
- Initial dataset release with 10 industry directories and 49 TSV files
- Coverage: Accommodation & Food, Administrative Support, Arts & Recreation, Education, Finance & Insurance, Healthcare & Social, Listed Companies, Public Administration, Transportation & Storage, Wholesale & Retail
