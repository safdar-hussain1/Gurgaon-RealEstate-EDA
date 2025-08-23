# Gurgaon Real Estate — EDA Audit & Validation Report

## 1) Files verified

- Original CSV: `Gurgaon_RealEstate.csv` — **3803 rows × 23 cols**
- Cleaned CSV: `Gurgaon_RealEstate_cleaned.csv` — **3371 rows × 24 cols**

## 2) Quick health summary

- Duplicate rows in original: **126**
- Overall missing cells: **orig: 6996 (7.998%)**, **cleaned: 4270 (5.278%)**

## 3) Columns

- Expected columns present in original (18): property_type, society, sector, price, price_per_sqft, area, bedroom, bathroom, balcony, facing, built_up_area, super_built_up_area, carpet_area, pooja_room, study_room, servant_room, furnishing_type, luxury_score
- Expected columns present in cleaned (18): property_type, society, sector, price, price_per_sqft, area, bedroom, bathroom, balcony, facing, built_up_area, super_built_up_area, carpet_area, pooja_room, study_room, servant_room, furnishing_type, luxury_score
- ✅ No expected columns were lost in the cleaned file.

## 4) Missingness (by column)

- A full CSV with per-column missingness before vs after cleaning was saved to `EDA_missing_summary.csv`.

Top-15 columns by missing % (after cleaning):

|                     |   missing_count_orig |   missing_count_cleaned |   missing_pct_orig |   missing_pct_cleaned |
|:--------------------|---------------------:|------------------------:|-------------------:|----------------------:|
| super_built_up_area |                 1888 |                    1629 |              49.65 |                 48.32 |
| carpet_area         |                 1859 |                    1602 |              48.88 |                 47.52 |
| facing              |                 1105 |                     980 |              29.06 |                 29.07 |
| floornum            |                   19 |                      16 |               0.5  |                  0.47 |
| price               |                   18 |                      14 |               0.47 |                  0.42 |
| price_per_sqft      |                   18 |                      14 |               0.47 |                  0.42 |
| area                |                   18 |                      14 |               0.47 |                  0.42 |
| society             |                    1 |                       1 |               0.03 |                  0.03 |
| built_up_area       |                 2070 |                       0 |              54.43 |                  0    |
| property_type       |                    0 |                       0 |               0    |                  0    |
| sector              |                    0 |                       0 |               0    |                  0    |
| areawithtype        |                    0 |                       0 |               0    |                  0    |
| bedroom             |                    0 |                       0 |               0    |                  0    |
| bathroom            |                    0 |                       0 |               0    |                  0    |
| balcony             |                    0 |                       0 |               0    |                  0    |

## 5) Outliers (IQR method)

- We computed IQR-based outliers on all numeric columns present in both files.
- A full CSV comparison table was saved to `EDA_outlier_comparison.csv`.

| feature             |   orig_total_outliers |   clean_total_outliers |   delta_outliers |
|:--------------------|----------------------:|-----------------------:|-----------------:|
| bedroom             |                   143 |                      0 |             -143 |
| bathroom            |                   127 |                     11 |             -116 |
| pooja_room          |                   663 |                    558 |             -105 |
| study_room          |                   721 |                    617 |             -104 |
| floornum            |                    84 |                      0 |              -84 |
| price               |                   432 |                    358 |              -74 |
| super_built_up_area |                    88 |                     14 |              -74 |
| price_per_sqft      |                   367 |                    304 |              -63 |
| area                |                   220 |                    158 |              -62 |
| others              |                   421 |                    360 |              -61 |
| store_room          |                   344 |                    296 |              -48 |
| carpet_area         |                    77 |                     56 |              -21 |
| furnishing_type     |                     0 |                      0 |                0 |
| luxury_score        |                     0 |                      0 |                0 |
| servant_room        |                     0 |                      0 |                0 |
| built_up_area       |                   127 |                   1126 |              999 |

## 6) Binary-feature compliance (cleaned)

- `pooja_room`: ✅ values restricted to 0/1
- `study_room`: ✅ values restricted to 0/1
- `storeroom`: (not present)
- `servant_room`: ✅ values restricted to 0/1

## 7) Distribution shifts (orig → cleaned)

Key numeric features — mean/median/std before vs after cleaning:

| feature             |   orig_mean |   clean_mean |    orig_std |   clean_std |   orig_median |   clean_median |   orig_n |   clean_n |
|:--------------------|------------:|-------------:|------------:|------------:|--------------:|---------------:|---------:|----------:|
| price               |     2.5058  |      2.25436 |     2.95012 |     2.54401 |           1.5 |           1.45 |     3785 |      3357 |
| price_per_sqft      | 13800.2     |  11919       | 23052       | 10360.5     |        9000   |        8784    |     3785 |      3357 |
| area                |  2846       |   1840.52    | 22783.3     |  1146.18    |        1725   |        1666    |     3785 |      3357 |
| built_up_area       |  2360.24    |   1861.54    | 17719.6     |   904.245   |        1650   |        1861.54 |     1733 |      3371 |
| super_built_up_area |  1921.66    |   1824.84    |   767.16    |   559.585   |        1828   |        1810    |     1915 |      1742 |
| carpet_area         |  2483.47    |   1397.62    | 22375.2     |   926.342   |        1294   |        1262    |     1944 |      1769 |
| bedroom             |     3.33815 |      3.04183 |     1.87673 |     1.07094 |           3   |           3    |     3803 |      3371 |
| bathroom            |     3.40547 |      3.11896 |     1.93046 |     1.2192  |           3   |           3    |     3803 |      3371 |
| luxury_score        |    70.9479  |     71.4586  |    52.8218  |    53.1831  |          58   |          59    |     3803 |      3371 |

## 8) Verdict & recommendations

• Missingness reduced or unchanged ✅
• Row count changed: 3803 → 3371 (expected if duplicate/outlier trimming applied)
• No expected columns lost ✅
• Outliers not reduced under IQR ⚠️ (review winsorization / trim thresholds)