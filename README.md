# HK Domain Resources

A curated collection of Hong Kong domain resources organized by industry sectors. This repository contains structured data (TSV format) of domains for various Hong Kong institutions and organizations.

本儲存庫是一個按行業分類整理的香港域名資源精選集,包含各類香港機構和組織的結構化數據(TSV 格式)。

---

## 📊 Statistics | 統計資料

- **Total Industries Covered | 涵蓋行業:** 11
- **Last Updated | 最後更新:** 2026-01-15

---

## 📋 Contents | 目錄

### 🏨 Accommodation & Food Services | 住宿及餐飲業
**Directory:** `accommodation_food/`

- **Food & Restaurants | 餐飲** - `food_hkrma_member.tsv`  
  HKRMA member restaurants and food service providers | 香港零售管理協會會員餐飲及食品服務提供者

---

### 🧑‍💼 Administrative & Support Services | 行政及支援服務業
**Directory:** `administrative_support/`

Administrative and business support services | 行政及商業支援服務

---

### 🎭 Arts, Entertainment & Recreation | 藝術、娛樂及康樂業
**Directory:** `arts_recreation/`

- **Tourism & Travel | 旅遊及旅行** - `tourism_tichk_travel_agent.tsv`  
  TIC member travel agents | 旅遊業議會會員旅行社

---

### 🎓 Education | 教育業
**Directory:** `education/`

- **Primary Schools - DSS | 小學 - 直資** - `education_primary_dss.tsv`
- **Primary Schools - Aided | 小學 - 資助** - `education_primary_aided.tsv`
- **Primary Schools - Private | 小學 - 私立** - `education_primary_private.tsv`
- **Primary Schools - Government | 小學 - 官立** - `education_primary_government.tsv`
- **Secondary Schools - DSS | 中學 - 直資** - `education_secondary_dss.tsv`
- **Secondary Schools - Aided | 中學 - 資助** - `education_secondary_aided.tsv`
- **Secondary Schools - Private | 中學 - 私立** - `education_secondary_private.tsv`
- **Secondary Schools - Government | 中學 - 官立** - `education_secondary_government.tsv`
- **Higher Education - iPass | 高等教育 - iPass** - `education_ipass_higher_diploma.tsv`
- **Degree Awarding (Non-UGC) | 學位頒授(非教資會)** - `education_degree_awarding_nonugc.tsv`

---

### 💰 Finance & Insurance | 金融及保險業
**Directory:** `finance_insurance/`

- **Banking & Payments | 銀行及支付** - `banking_payments.tsv`
- **Insurance | 保險** - `insurance.tsv`
- **Pension Trustees | 退休金信託** - `pension_trustees.tsv`
- **Money Service Operators | 貨幣服務經營者** - `money_service_operator.tsv`
- **Capital Markets | 資本市場** - `capital_markets.tsv`
- **Market Infrastructure | 市場基建** - `market_infrastructure.tsv`
- **Industry Association | 行業協會** - `industry_association.tsv`
- **Stored Value Facilities | 儲值支付工具** - `stored_value_facility.tsv`

---

### 🏥 Healthcare & Social Work | 人類醫療保健及社會工作業
**Directory:** `healthcare_social/`

- **Healthcare | 醫療** - `healthcare.tsv`
- **Private Hospitals | 私家醫院** - `orphf_private_hospital.tsv`
- **Nursing Homes | 護養院** - `orphf_nursing_home.tsv`
- **Day Procedure Centres | 日間醫療中心** - `orphf_day_procedure_centre.tsv`
- **Small Practice Clinics | 小型診所** - `orphf_small_practice_clinic.tsv`
- **Clinics | 診所** - `orphf_clinic.tsv`
- **NGOs | 非政府組織** - `ngo_hkcss_ctgoodjobs.tsv`

---

### 📈 Listed Companies | 上市公司
**Directory:** `listed_companies/`

- **Capital Markets | 資本市場** - `capital_markets.tsv`  
  HKEX listed companies | 香港交易所上市公司

---

### 🏛️ Public Administration | 公共行政
**Directory:** `public_administration/`

- **Government | 政府** - `government.tsv`
- **Insurance Regulation | 保險監管** - `insurance.tsv`
- **Law & Justice | 法律及司法** - `law_govhk.tsv`
- **Trade | 貿易** - `trade_govhk.tsv`
- **Labour | 勞工** - `labour_govhk.tsv`
- **Innovation | 創新科技** - `innovation_govhk.tsv`
- **Tourism | 旅遊** - `tourism_govhk.tsv`
- **Housing | 房屋** - `housing_govhk.tsv`
- **Transport | 運輸** - `transport_govhk.tsv`
- **Regulators & Statutory Bodies | 監管機構及法定機構** - `regulators_statutory.tsv`

---

### 🚚 Transportation & Storage | 運輸、倉庫及速遞服務業
**Directory:** `transportation_storage/`

- **Logistics | 物流** - `logistics_haffa_member.tsv`  
  HAFFA member freight forwarders | 貨運物流業協會會員

---

### 🛒 Wholesale & Retail Trade | 批發及零售業
**Directory:** `wholesale_retail/`

- **Retail | 零售** - `retail_hkrma_member.tsv`
- **Telecommunications | 電訊** - `telecom_hkrma_member.tsv`
- **Other Retail | 其他零售** - `other_hkrma_member.tsv`

---

## 📊 Data Format | 數據格式

All data files are in **TSV (Tab-Separated Values)** format for easy parsing and compatibility with various data processing tools.

所有數據檔案均為 **TSV(Tab-Separated Values,以製表符分隔)** 格式,方便解析並與各種數據處理工具兼容。

### Typical Fields | 典型欄位:
- **industry** - Industry sector | 行業分類
- **category** - Sub-category | 子分類
- **name** - Organization name | 機構名稱
- **domain** - Domain name | 域名
- **source** - Data source | 數據來源
- **dataset** - Associated datasets | 相關數據集

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

---

## 💻 Usage Examples | 使用範例

### Load TSV file (Python)
```python
import pandas as pd

# Load education data
df = pd.read_csv('education/education_primary_aided.tsv', sep='\t')
print(df.head())

# Load financial sector data
df_finance = pd.read_csv('finance_insurance/banking_payments.tsv', sep='\t')
print(df_finance.head())
```

### Command line processing
```bash
# Count entries in a file
wc -l finance_insurance/insurance.tsv

# Search for specific domain
grep "hsbc" finance_insurance/banking_payments.tsv

# List all TSV files
find . -name "*.tsv" -type f

# Count total entries across all files
find . -name "*.tsv" -exec wc -l {} + | tail -1
```

### Explore directory structure
```bash
# List all industries
ls -d */

# List files in finance sector
ls finance_insurance/

# View file contents
cat education/education_primary_aided.tsv | head
```

---

## 📝 Contributing | 貢獻

Contributions are welcome! If you notice any missing domains or have updates to existing entries:

歡迎貢獻!如果您發現任何遺漏的域名或需要更新現有條目:

1. Fork this repository | Fork 本儲存庫
2. Add or update entries in the appropriate TSV file under the correct industry directory | 在正確的行業目錄下的適當 TSV 檔案中添加或更新條目
3. Ensure data follows the existing format | 確保數據遵循現有格式
4. Submit a pull request with a clear description | 提交帶有清晰描述的 pull request

### Guidelines | 指引:
- Maintain TSV format consistency | 保持 TSV 格式一致性
- Verify domain accuracy | 驗證域名準確性
- Include official sources when possible | 盡可能包含官方來源
- Place files in the correct industry directory | 將檔案放置在正確的行業目錄中
- One logical change per PR | 每個 PR 一個邏輯變更

---

## 📄 License | 授權

This data is provided for research and informational purposes. Please ensure appropriate use of this data in compliance with applicable laws and regulations.

這些數據僅供研究和參考之用。請確保適當使用這些數據,並遵守適用的法律法規。

---

## ⚠️ Disclaimer | 免責聲明

- This repository is for **informational and research purposes only**  
  本儲存庫僅供**參考和研究之用**

- The accuracy of the data is provided **as-is**, and maintainers are not responsible for any outdated or incorrect information  
  數據的準確性**按原樣提供**,維護者對任何過時或不正確的資訊概不負責

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
- [HKRMA - Hong Kong Retail Management Association](https://www.hkrma.org/)
- [HAFFA - Hong Kong Association of Freight Forwarding and Logistics](https://www.haffa.com.hk/)

---

**Maintained by | 維護者:** [@FusionPlmH](https://github.com/FusionPlmH)  
**Last Updated | 最後更新:** 2026-01-15