# Data dictionary — `gurgaon_properties.csv`

3,803 listings × 23 columns. Cleaned column names (used in `data/processed/`) are shown alongside the raw names where they differ.

| Raw column | Cleaned name | Type | Description |
|---|---|---|---|
| `property_type` | — | categorical | `flat` or `house` (independent house / builder floor) |
| `society` | — | categorical (676 values) | Housing society / project name |
| `sector` | — | categorical (104 values) | Gurgaon sector of the listing |
| `price` | — | float | Asking price in **₹ crore** (1 crore = ₹10,000,000) |
| `price_per_sqft` | — | float | Asking price per sq. ft. in ₹ |
| `area` | — | float | Headline area in sq. ft. (consistent with `price / price_per_sqft`) |
| `areaWithType` | `area_with_type` | string | Free-text area breakdown as shown on the portal |
| `bedRoom` | `bedrooms` | int | Number of bedrooms |
| `bathroom` | `bathrooms` | int | Number of bathrooms |
| `balcony` | — | ordered categorical | Number of balconies: `0`, `1`, `2`, `3`, `3+` |
| `floorNum` | `floor_num` | float | Floor the unit is on (0 = ground) |
| `facing` | — | categorical | Direction the property faces (29% missing) |
| `agePossession` | `age_possession` | categorical | `Under Construction`, `New Property`, `Relatively New`, `Moderately Old`, `Old Property` (`Undefined` → missing) |
| `super_built_up_area` | — | float | Super built-up area, sq. ft. (~50% missing) |
| `built_up_area` | — | float | Built-up area, sq. ft. (~54% missing) |
| `carpet_area` | — | float | Carpet area, sq. ft. (~49% missing) |
| `study room` | `has_study_room` | binary | 1 if the listing includes a study room |
| `servant room` | `has_servant_room` | binary | 1 if the listing includes a servant room |
| `store room` | `has_store_room` | binary | 1 if the listing includes a store room |
| `pooja room` | `has_pooja_room` | binary | 1 if the listing includes a pooja room |
| `others` | `has_other_rooms` | binary | 1 if other extra rooms are listed |
| `furnishing_type` | — | categorical | Raw codes 0/1/2 → `unfurnished` / `semi-furnished` / `furnished` |
| `luxury_score` | — | int (0–174) | Portal-derived score counting luxury amenities |
