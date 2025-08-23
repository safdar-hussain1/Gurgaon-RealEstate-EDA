Here you go — copy-paste this into your `README.md` on GitHub.

---

# Gurgaon Real Estate — Consolidated EDA

A complete, reproducible exploratory data analysis (EDA) for the Gurgaon real-estate dataset.
This repo includes two Jupyter notebooks (baseline and enhanced v2), the original & cleaned CSVs, a PDF report with plots, and audit tables.

---

## 📦 What’s inside

```
.
├─ Gurgaon_RealEstate_EDA_Consolidated.ipynb      # v1: consolidated EDA (baseline)
├─ Gurgaon_RealEstate_EDA_Consolidated_v2.ipynb   # v2: advanced add-ons (validations, heatmap, MAD, pivots, etc.)
├─ Gurgaon_RealEstate.csv                         # original dataset
├─ Gurgaon_RealEstate_cleaned.csv                 # cleaned dataset (after outlier handling & fixes)
├─ Gurgaon_RealEstate_EDA_Report.pdf              # PDF report with screenshots & commentary
├─ EDA_outlier_comparison.csv                     # IQR outlier comparison (orig vs cleaned)
├─ EDA_missing_summary.csv                        # per-column missingness summary (orig vs cleaned)
├─ data_dictionary.csv                            # auto-generated: dtypes, %missing, examples
├─ requirements.txt                               # Python dependencies
└─ README.md
```

> If any file is >100 MB, GitHub will reject it. Use Git LFS or exclude large raw data.

---

## 🚀 Quickstart

### 1) Install dependencies

```bash
# (optional) create a virtual environment
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
# .venv\Scripts\activate

# install deps
pip install --upgrade pip
pip install -r requirements.txt
```

> Optional (for one cell in v2):
>
> ```bash
> pip install statsmodels
> ```

### 2) Run a notebook

Open **Gurgaon\_RealEstate\_EDA\_Consolidated\_v2.ipynb** (recommended) or v1 in Jupyter/Colab and run top-to-bottom.

* If your CSVs are in the repo root (as above), it works out of the box.
* Otherwise, update `CSV_PATH` near the top of the notebook.

### 3) Outputs

* The **cleaned CSV** is saved as `Gurgaon_RealEstate_cleaned.csv`.
* A full **PDF report** is provided: `Gurgaon_RealEstate_EDA_Report.pdf`.

---

## 🧭 What the EDA covers

**Core (v1)**

* Column normalization & duplicate removal
* Descriptives (dtypes, `describe()`, cardinalities)
* Missing-data matrix (+ optional dendrogram if SciPy is available)
* Society / Sector distributions, frequency bins
* Price & Price-per-sqft: histograms, boxplots, quantile bins
* Bedrooms / Bathrooms / Balcony / Floor / Facing distributions & crosstabs
* Built-up / Super-built-up / Carpet area summaries + **ratio-based imputation**
* Multivariate: Price vs key features (scatter; pure matplotlib)
* Outliers: IQR & Z-score tables + **winsorization / trim** strategies
* Binary features standardized to 0/1
* **Artifacts**: cleaned CSV

**Advanced add-ons (v2)**

* Reproducibility banner (versions + seed)
* Data dictionary (`data_dictionary.csv`): dtype, %missing, unique count, examples
* **Validation rules**:

  * Non-negative checks for numeric features
  * Area order: `super_built_up ≥ built_up ≥ carpet`
  * Sanity: `price ≈ ppsf × built_up_area` (tolerance flagged)
* Rare-category bucketing for **sector** & **furnishing\_type** (top-15 plots)
* Numeric **correlation heatmap** (matplotlib)
* **Market segmentation**: median Price by Sector × Bedrooms, Top-10 sectors by volume
* **MAD-based outliers** for Price & PPSF (robust to heavy tails)
* Helpers: figure saver, quick OLS if `statsmodels` is installed
* Optional monthly trends if date-like columns exist

---

## 📑 Regenerating the PDF report

The repository includes `Gurgaon_RealEstate_EDA_Report.pdf`.
To regenerate it yourself:

1. Ensure both `Gurgaon_RealEstate.csv` and `Gurgaon_RealEstate_cleaned.csv` are present in the repo root.
2. Run the PDF generation cell/script (matplotlib-only).
3. The output is an A4 multi-page PDF with: missingness matrices (orig & cleaned), key distributions, price vs features, a data-quality verdict, and outlier tables.

> You can also save plots directly from the notebook using the helper `save_current_fig("name")` (v2 section A8).

---

## 🧪 Reproducibility

* Python: 3.9+
* Libraries: `numpy`, `pandas`, `matplotlib`, `scipy` (optional), `statsmodels` (optional)
* Install all required packages with:

```bash
pip install -r requirements.txt
```

---

## ✅ Data quality checklist

* Missingness reduced or controlled in the cleaned dataset
* No negative values in numeric columns
* **Area order** respected: `super_built_up ≥ built_up ≥ carpet`
* **Price sanity** vs `ppsf × built_up_area` (only small deviations)
* Outliers reduced post-cleaning (IQR and/or MAD)
* Binary features are strictly 0/1
* Correlations and segment medians make domain sense

---

## 🧩 Troubleshooting

* **File not found** → update `CSV_PATH` in the notebook.
* **Plots don’t show** → run cells sequentially in Jupyter; `%matplotlib inline` is implicit.
* **Very large CSVs** → track with Git LFS or avoid committing them.
* **Weird PPSF/Price** → check units (₹ vs lakh), and area units (sqft vs sqm).

---

## 📄 License

Add your preferred license (e.g., MIT). If unspecified, assume “all rights reserved.”

---

## 🙌 Acknowledgements

Thanks to open real-estate data sources and community references used to validate basic assumptions and ranges.

---
