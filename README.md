# HK Domain Resources

A curated collection of Hong Kong domain resources organized by industry sectors.  This repository contains structured data (TSV format) of domains for various Hong Kong institutions and organizations.

本儲存庫是一個按行業分類整理的香港域名資源精選集，包含各類香港機構和組織的結構化數據（TSV 格式）。

---

## 📊 Statistics | 統計資料

- **Total Categories | 分類總數:** 10
- **Industries Covered | 涵蓋行業:** 10+
- **Last Updated | 最後更新:** 2026-01-15

---

## 📋 Contents | 目錄

### 🏨 Accommodation & Food Services | 住宿及餐飲服務
**Directory:** `accommodation_food/`

Hotels, restaurants, and food service establishments | 酒店、餐廳及餐飲服務機構

### 🏢 Administrative & Support Services | 行政及支援服務
**Directory:** `administrative_support/`

Administrative, business support, and professional services | 行政、商業支援及專業服務

### 🎨 Arts, Entertainment & Recreation | 藝術、娛樂及康樂
**Directory:** `arts_recreation/`

Cultural, entertainment, and recreational organizations | 文化、娛樂及康樂組織

### 🎓 Education | 教育
**Directory:** `education/`

Educational institutions including primary schools, secondary schools, universities and colleges | 教育機構，包括小學、中學、大學及專上學院

### 🏥 Healthcare & Social Assistance | 醫療保健及社會服務
**Directory:** `healthcare_social/`

Healthcare providers, medical institutions, and social service organizations | 醫療服務提供者、醫療機構及社會服務組織

### 📈 Listed Companies | 上市公司
**Directory:** `listed_companies/`

Hong Kong Stock Exchange listed companies and publicly traded entities | 香港交易所上市公司及公開交易實體

### 🏛️ Public Administration | 公共行政
**Directory:** `public_administration/`

Government departments, agencies, and public sector organizations | 政府部門、機構及公共部門組織

### 🚢 Transportation & Storage | 運輸及倉儲
**Directory:** `transportation_storage/`

Transportation providers, logistics companies, and storage facilities | 運輸服務提供者、物流公司及倉儲設施

### 🛒 Wholesale & Retail Trade | 批發及零售貿易
**Directory:** `wholesale_retail/`

Wholesale distributors and retail establishments | 批發分銷商及零售商店

---

## 📊 Data Format | 數據格式

All data files are in **TSV (Tab-Separated Values)** format for easy parsing and compatibility with various data processing tools.

所有數據檔案均為 **TSV（Tab-Separated Values，以製表符分隔）** 格式，方便解析並與各種數據處理工具兼容。

### Typical Fields | 典型欄位: 
- Domain name | 域名
- Organization name | 機構名稱
- Additional metadata (varies by sector) | 其他元數據（因行業而異）

---

## 📁 Repository Structure | 儲存庫結構

```
HK-Domain-Resources/
├── accommodation_food/       # 住宿及餐飲服務
├── administrative_support/   # 行政及支援服務
├── arts_recreation/          # 藝術、娛樂及康樂
├── education/                # 教育
├── healthcare_social/        # 醫療保健及社會服務
├── listed_companies/         # 上市公司
├── public_administration/    # 公共行政
├── transportation_storage/   # 運輸及倉儲
├── wholesale_retail/         # 批發及零售貿易
└── README.md
```

---

## 🔍 Use Cases | 使用場景

- **Domain Research & Analysis | 域名研究與分析**  
  Analyze domain patterns and trends in Hong Kong sectors | 分析香港各行業的域名模式和趨勢

- **Security Research & Threat Intelligence | 安全研究與威脅情報**  
  Build allowlists/blocklists for phishing detection | 建立允許/封鎖名單以偵測釣魚攻擊  
  Monitor domain spoofing attempts | 監測域名欺騙嘗試

- **Network Monitoring & Filtering | 網絡監控與過濾**  
  Configure enterprise firewalls and content filters | 配置企業防火牆和內容過濾器

- **Data Analytics & Visualization | 數據分析與可視化**  
  Create industry insights and reports | 創建行業洞察和報告

- **Educational Reference | 教育參考**  
  Research institutional digital presence | 研究機構的數字化存在

- **Market Intelligence | 市場情報**  
  Track industry participants and market landscape | 追蹤行業參與者和市場格局

---

## 💻 Usage Examples | 使用範例

### Load TSV file (Python)
```python
import pandas as pd

# Load education sector domains
df = pd.read_csv('education/education.tsv', sep='\t')
print(df.head())

# Load listed companies
df_listed = pd.read_csv('listed_companies/listed.tsv', sep='\t')
print(df_listed.info())
```

### Command line processing
```bash
# Count entries in a specific sector
wc -l education/*.tsv

# Search for specific domain across all sectors
find . -name "*.tsv" -exec grep -l "hku.hk" {} \;

# Combine all files from a sector
cat education/*.tsv > education_combined.tsv

# List all TSV files in the repository
find . -name "*.tsv"
```

### Data Analysis (Python)
```python
import pandas as pd
import glob

# Load all TSV files from a directory
sector_path = 'education/*.tsv'
all_files = glob.glob(sector_path)

df_list = []
for filename in all_files:
    df = pd.read_csv(filename, sep='\t')
    df['source_file'] = filename
    df_list.append(df)

# Combine all dataframes
combined_df = pd.concat(df_list, ignore_index=True)
print(f"Total domains: {len(combined_df)}")
```

---

## 📝 Contributing | 貢獻

Contributions are welcome! If you notice any missing domains or have updates to existing entries: 

歡迎貢獻！如果您發現任何遺漏的域名或需要更新現有條目：

1. Fork this repository | Fork 本儲存庫
2. Add or update entries in the appropriate TSV file under the relevant directory | 在相關目錄下的適當 TSV 檔案中添加或更新條目
3. Ensure data follows the existing format | 確保數據遵循現有格式
4. Submit a pull request with a clear description | 提交帶有清晰描述的 pull request

### Guidelines | 指引: 
- Maintain TSV format consistency | 保持 TSV 格式一致性
- Verify domain accuracy | 驗證域名準確性
- Include official sources when possible | 盡可能包含官方來源
- One logical change per PR | 每個 PR 一個邏輯變更
- Place files in the correct category directory | 將檔案放置在正確的分類目錄中

---

## 📄 License | 授權

This data is provided for research and informational purposes.  Please ensure appropriate use of this data in compliance with applicable laws and regulations.

這些數據僅供研究和參考之用。請確保適當使用這些數據，並遵守適用的法律法規。

---

## ⚠️ Disclaimer | 免責聲明

- This repository is for **informational and research purposes only**  
  本儲存庫僅供**參考和研究之用**

- The accuracy of the data is provided **as-is**, and maintainers are not responsible for any outdated or incorrect information  
  數據的準確性**按原樣提供**，維護者對任何過時或不正確的資訊概不負責

- This is **not** an official government or industry resource  
  這**不是**官方政府或行業資源

- Domain inclusion does not imply endorsement or verification  
  域名的收錄並不意味著認可或驗證

- Users should independently verify information for critical applications  
  用戶應獨立驗證關鍵應用的資訊

---

## 🔗 Related Resources | 相關資源

- [HKIRC - Hong Kong Internet Registration Corporation](https://www.hkirc.hk/)
- [HKEX - Hong Kong Exchanges and Clearing](https://www.hkex.com.hk/)
- [GovHK - Hong Kong Government Portal](https://www.gov.hk/)
- [Hong Kong Trade Development Council](https://www.hktdc.com/)
- [Companies Registry Hong Kong](https://www.cr.gov.hk/)

---

**Maintained by | 維護者:** [@FusionPlmH](https://github.com/FusionPlmH)  
**Last Updated | 最後更新:** 2026-01-15