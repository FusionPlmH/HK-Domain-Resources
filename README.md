# HK Domain Resources

A curated collection of Hong Kong domain resources organized by industry sectors. This repository contains structured data (TSV format) of domains for various Hong Kong institutions and organizations.

本儲存庫是一個按行業分類整理的香港域名資源精選集，包含各類香港機構和組織的結構化數據（TSV 格式）。

---

## 📊 Statistics | 統計資料

- **Total Categories | 分類總數:** 10
- **Total Files | 檔案總數:** 25+
- **Last Updated | 最後更新:** 2026-01-15

---

## 📋 Contents | 目錄

### 🏨 Accommodation & Food Services | 住宿及餐飲服務
**Directory:** `accommodation_food/`

- **food_hkrma_member.tsv** - Hong Kong Retail Management Association (HKRMA) member food service establishments | 香港零售管理協會成員餐飲服務機構
  - Major chains: McDonald's, KFC, Maxim's, Café de Coral, Pacific Coffee, etc.

### 🏢 Administrative & Support Services | 行政及支援服務
**Directory:** `administrative_support/`

- **recruitment_eaa_agency.tsv** - Employment agencies registered with the Labour Department | 勞工處註冊職業介紹所
  - Recruitment consultancies and employment agencies | 招聘顧問及職業介紹所

### 🎨 Arts, Entertainment & Recreation | 藝術、娛樂及康樂
**Directory:** `arts_recreation/`

- **tourism_tichk_travel_agent.tsv** - Travel Industry Council of Hong Kong (TIC) member travel agents | 香港旅遊業議會會員旅行社

### 🎓 Education | 教育
**Directory:** `education/`

#### Primary Schools | 小學
- **education_primary_government.tsv** - Government-run primary schools | 官立小學
- **education_primary_aided.tsv** - Government-aided primary schools | 資助小學
- **education_primary_dss.tsv** - Direct Subsidy Scheme (DSS) primary schools | 直資小學
- **education_primary_private.tsv** - Private and international primary schools | 私立及國際小學

#### Secondary Schools | 中學
- **education_secondary_government.tsv** - Government-run secondary schools | 官立中學
- **education_secondary_aided.tsv** - Government-aided secondary schools | 資助中學
- **education_secondary_dss.tsv** - Direct Subsidy Scheme (DSS) secondary schools | 直資中學
- **education_secondary_private.tsv** - Private and international secondary schools | 私立及國際中學

#### Higher Education | 高等教育
- **education_degree_awarding_nonugc.tsv** - Degree-awarding institutions (non-UGC) | 非教資會學位頒授院校
- **education_ipass_higher_diploma.tsv** - iPASS higher diploma programs | iPASS 高級文憑課程

### 🏥 Healthcare & Social Assistance | 醫療保健及社會服務
**Directory:** `healthcare_social/`

- **healthcare.tsv** - Healthcare institutions and medical councils | 醫療機構及醫療委員會
- **orphf_nursing_home.tsv** - Residential care homes for the elderly (ORPHF registered) | 安老院舍（社署註冊）
- **ngo_hkcss_ctgoodjobs.tsv** - Non-governmental organizations (NGOs) | 非政府組織
  - Social service organizations from HKCSS directory | 社聯目錄的社會服務機構

### 📈 HKEX Listed Companies | 港交所上市公司
**Directory:** `hkex_listed_companies/`

Hong Kong Stock Exchange listed companies and publicly traded entities | 香港交易所上市公司及公開交易實體

### 🏛️ Public Administration | 公共行政
**Directory:** `public_administration/`

- **housing_govhk.tsv** - Housing and property-related government departments | 房屋及物業相關政府部門
  - Housing Authority, Buildings Department, Lands Department, etc.
- **innovation_govhk.tsv** - Innovation and technology government bodies | 創新科技政府機構
  - Cyberport, HKSTP, ASTRI, Innovation and Technology Bureau, etc.
- **social-welfare_govhk.tsv** - Social welfare government departments | 社會福利政府部門
  - Social Welfare Department, Labour and Welfare Bureau, etc.

### 🚢 Transportation & Storage | 運輸及倉儲
**Directory:** `transportation_storage/`

- **logistics_haffa_member.tsv** - Hong Kong Association of Freight Forwarding and Logistics (HAFFA) members | 香港貨運物流業協會會員
  - Freight forwarders and logistics companies | 貨運代理及物流公司

### 🛒 Wholesale & Retail Trade | 批發及零售貿易
**Directory:** `wholesale_retail/`

- **telecom_hkrma_member.tsv** - HKRMA member telecommunications retail companies | 零管協會員電訊零售公司
  - Major telecom operators: HKT, CSL, SmarTone, China Mobile HK

---

## 📁 Repository Structure | 儲存庫結構

```
HK-Domain-Resources/
├── accommodation_food/
│   └── food_hkrma_member.tsv
├── administrative_support/
│   └── recruitment_eaa_agency.tsv
├── arts_recreation/
│   └── tourism_tichk_travel_agent.tsv
├── education/
│   ├── education_primary_government.tsv
│   ├── education_primary_aided.tsv
│   ├── education_primary_dss.tsv
│   ├── education_primary_private.tsv
│   ├── education_secondary_government.tsv
│   ├── education_secondary_aided.tsv
│   ├── education_secondary_dss.tsv
│   ├── education_secondary_private.tsv
│   ├── education_degree_awarding_nonugc.tsv
│   └── education_ipass_higher_diploma.tsv
├── healthcare_social/
│   ├── healthcare.tsv
│   ├── orphf_nursing_home.tsv
│   └── ngo_hkcss_ctgoodjobs.tsv
├── hkex_listed_companies/
├── public_administration/
│   ├── housing_govhk.tsv
│   ├── innovation_govhk.tsv
│   └── social-welfare_govhk.tsv
├── transportation_storage/
│   └── logistics_haffa_member.tsv
├── wholesale_retail/
│   └── telecom_hkrma_member.tsv
└── README.md
```

---

## 📊 Data Format | 數據格式

All data files are in **TSV (Tab-Separated Values)** format for easy parsing and compatibility with various data processing tools.

所有數據檔案均為 **TSV（Tab-Separated Values，以製表符分隔）** 格式，方便解析並與各種數據處理工具兼容。

### Standard Fields | 標準欄位:
- **industry** - Industry classification | 行業分類
- **category** - Sub-category | 子分類
- **name** - Organization name | 機構名稱
- **domain** - Domain name | 域名
- **source** - Data source | 數據來源
- **dataset** - Source dataset file | 來源數據集檔案

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

- **Compliance & Due Diligence | 合規與盡職調查**  
  Verify official domains for business processes | 驗證業務流程的官方域名

---

## 💻 Usage Examples | 使用範例

### Load TSV file (Python)
```python
import pandas as pd

# Load education sector domains
df = pd.read_csv('education/education_primary_government.tsv', sep='\t')
print(df.head())
print(f"Total schools: {len(df)}")

# Filter by category
print(df[df['category'] == 'education_primary_government'])
```

### Command line processing
```bash
# Count entries in a specific file
wc -l education/education_primary_government.tsv

# Search for specific domain across all sectors
find . -name "*.tsv" -exec grep -l "edu.hk" {} \;

# Combine all education files
cat education/*.tsv > education_combined.tsv

# Extract just domains from a file
cut -f4 healthcare_social/healthcare.tsv

# List all unique industries
find . -name "*.tsv" -exec awk -F'\t' 'NR>1 {print $1}' {} \; | sort -u
```

### Data Analysis (Python)
```python
import pandas as pd
import glob

# Load all TSV files from education directory
all_files = glob.glob('education/*.tsv')

df_list = []
for filename in all_files:
    df = pd.read_csv(filename, sep='\t')
    df['source_file'] = filename
    df_list.append(df)

# Combine all dataframes
combined_df = pd.concat(df_list, ignore_index=True)
print(f"Total education domains: {len(combined_df)}")

# Group by category
category_counts = combined_df.groupby('category').size()
print("\nDomains per category:")
print(category_counts)

# Find duplicate domains
duplicates = combined_df[combined_df.duplicated(['domain'], keep=False)]
print(f"\nDuplicate domains: {len(duplicates)}")
```

### Extract all domains to a simple list
```bash
# Create a plain text list of all domains
find . -name "*.tsv" -exec awk -F'\t' 'NR>1 {print $4}' {} \; | sort -u > all_domains.txt
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
- Maintain TSV format consistency (use tabs, not spaces) | 保持 TSV 格式一致性（使用製表符，而非空格）
- Verify domain accuracy before submission | 提交前驗證域名準確性
- Include official sources when possible | 盡可能包含官方來源
- One logical change per PR | 每個 PR 一個邏輯變更
- Place files in the correct category directory | 將檔案放置在正確的分類目錄中
- Follow the standard field structure | 遵循標準欄位結構

---

## 📄 License | 授權

This data is provided for research and informational purposes. Please ensure appropriate use of this data in compliance with applicable laws and regulations.

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

- Data is collected from publicly available sources  
  數據來自公開來源

---

## 🔗 Related Resources | 相關資源

### Official Government Portals | 官方政府入口網站
- [GovHK - Hong Kong Government Portal](https://www.gov.hk/)
- [Education Bureau (EDB)](https://www.edb.gov.hk/)
- [Social Welfare Department](https://www.swd.gov.hk/)
- [Labour Department](https://www.labour.gov.hk/)

### Industry Organizations | 行業組織
- [HKIRC - Hong Kong Internet Registration Corporation](https://www.hkirc.hk/)
- [HKEX - Hong Kong Exchanges and Clearing](https://www.hkex.com.hk/)
- [Hong Kong Trade Development Council](https://www.hktdc.com/)
- [Hong Kong Retail Management Association](https://www.hkrma.org/)
- [HAFFA - HK Association of Freight Forwarding and Logistics](https://www.haffa.com.hk/)
- [Travel Industry Council of Hong Kong](https://www.tichk.org/)

### Business Resources | 商業資源
- [Companies Registry Hong Kong](https://www.cr.gov.hk/)
- [Hong Kong Council of Social Service](https://www.hkcss.org.hk/)

---

## 📈 Data Sources | 數據來源

This repository aggregates data from various official and authoritative sources:

- Education Bureau (EDB) school location database
- GovHK directory
- HKEX listed companies
- Industry association membership directories (HKRMA, HAFFA, TIC)
- Labour Department employment agency registry
- Social Welfare Department private residential care homes registry
- Hong Kong Council of Social Service NGO directory

---

**Maintained by | 維護者:** [@FusionPlmH](https://github.com/FusionPlmH)  
**Last Updated | 最後更新:** 2026-01-15