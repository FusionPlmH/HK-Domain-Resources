# HK Domain Resources

A curated collection of Hong Kong domain resources organized by industry sectors. This repository contains structured data (TSV format) of domains for various Hong Kong institutions and organizations.

本儲存庫是一個按行業分類整理的香港域名資源精選集，包含各類香港機構和組織的結構化數據（TSV 格式）。

---

## 📊 Statistics | 統計資料

- **Total Files | 檔案總數:** 15
- **Industries Covered | 涵蓋行業:** 9+
- **Last Updated | 最後更新:** 2026-01-13

---

## 📋 Contents | 目錄

### 💰 Financial Sector | 金融業

- **Banking | 銀行業** - `bank.tsv`  
  Hong Kong banks and financial institutions | 香港銀行及金融機構

- **Financial Services | 金融服務** - `financial.tsv`  
  Financial service providers | 金融服務提供者

- **Insurance | 保險業** - `insurance.tsv`  
  Insurance companies | 保險公司

- **Payment Services | 支付服務** - `payment-fps.tsv`  
  FPS (Faster Payment System) participants | 轉數快參與機構

- **MPF Services | 強積金服務** - `mpfa.tsv`  
  Mandatory Provident Fund schemes | 強制性公積金計劃

### 🎓 Education Sector | 教育界

- **Complete Dataset | 完整數據集** - `education.tsv`  
  All education institutions | 所有教育機構

- **Primary Schools | 小學** - `education-primary.tsv`  
  Primary education institutions | 小學教育機構

- **Secondary Schools | 中學** - `education-secondary.tsv`  
  Secondary education institutions | 中學教育機構

- **Higher Education | 高等教育** - `education-higher-ed.tsv`  
  Universities and colleges | 大學及專上學院

### 🏛️ Public Sector | 公共部門

- **Government | 政府** - `government.tsv`  
  Government departments and agencies | 政府部門及機構

- **Healthcare | 醫療** - `healthcare.tsv`  
  Healthcare providers and medical institutions | 醫療服務提供者及醫療機構

### 📦 Logistics & Transport | 物流運輸

- **Freight & Logistics | 貨運物流** - `haffa.tsv`  
  Hong Kong Association of Freight Forwarding and Logistics members | 香港貨運物流業協會成員

### 🏢 Corporate & Market | 企業與市場

- **Listed Companies | 上市公司** - `listed-hkex.tsv`  
  Hong Kong Stock Exchange listed companies | 香港交易所上市公司

### 🤝 Non-Profit Organizations | 非牟利組織

- **NGOs | 非政府組織** - `ngo.tsv`  
  Non-governmental organizations | 非政府組織

---

## 📊 Data Format | 數據格式

All data files are in **TSV (Tab-Separated Values)** format for easy parsing and compatibility with various data processing tools.

所有數據檔案均為 **TSV（Tab-Separated Values，以製表符分隔）** 格式，方便解析並與各種數據處理工具兼容。

### Typical Fields | 典型欄位:
- Domain name | 域名
- Organization name | 機構名稱
- Additional metadata (varies by sector) | 其他元數據（因行業而異）

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

# Load bank domains
df = pd.read_csv('bank.tsv', sep='\t')
print(df.head())
```

### Command line processing
```bash
# Count entries
wc -l bank.tsv

# Search for specific domain
grep "hsbc" bank.tsv

# Combine all financial sector files
cat bank.tsv financial.tsv insurance.tsv > financial_all.tsv
```

---

## 📝 Contributing | 貢獻

Contributions are welcome! If you notice any missing domains or have updates to existing entries:

歡迎貢獻！如果您發現任何遺漏的域名或需要更新現有條目：

1. Fork this repository | Fork 本儲存庫
2. Add or update entries in the appropriate TSV file | 在適當的 TSV 檔案中添加或更新條目
3. Ensure data follows the existing format | 確保數據遵循現有格式
4. Submit a pull request with a clear description | 提交帶有清晰描述的 pull request

### Guidelines | 指引:
- Maintain TSV format consistency | 保持 TSV 格式一致性
- Verify domain accuracy | 驗證域名準確性
- Include official sources when possible | 盡可能包含官方來源
- One logical change per PR | 每個 PR 一個邏輯變更

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

---

## 🔗 Related Resources | 相關資源

- [HKIRC - Hong Kong Internet Registration Corporation](https://www.hkirc.hk/)
- [HKEX - Hong Kong Exchanges and Clearing](https://www.hkex.com.hk/)
- [GovHK - Hong Kong Government Portal](https://www.gov.hk/)

---

**Maintained by | 維護者:** [@FusionPlmH](https://github.com/FusionPlmH)  
**Last Updated | 最後更新:** 2026-01-13