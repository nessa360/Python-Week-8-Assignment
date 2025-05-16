# 🌍 COVID-19 Global Data Analysis

A comprehensive data analysis project exploring the global impact of the COVID-19 pandemic using the [Our World in Data](https://covid.ourworldindata.org/) dataset. The project covers data loading, preprocessing, exploratory data analysis, and visualization of key trends.

---

## 📁 Dataset Overview

- **Source:** [OWID COVID-19 Dataset](https://covid.ourworldindata.org/data/owid-covid-data.csv)
- **Total Records:** 429,435 rows
- **Features:** 67 columns including case numbers, deaths, hospitalizations, testing, vaccination rates, and more
- **Coverage:** Global — 255 unique locations (countries/regions)

---

## 🔧 Tools & Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 📊 Project Workflow

### 1. Data Loading
- Loaded directly from the OWID CSV repository.
- Initial shape of the dataset: `(429,435, 67)`

### 2. Data Exploration
- Inspected:
  - Column names
  - Data types
  - Unique locations
  - Missing values
  - Summary statistics

### 3. Data Cleaning
- Converted the `date` column to datetime format.
- Filtered out non-country rows (e.g., continents, EU, World).
- Selected 11 countries for focused analysis:
  - United States
  - India
  - Brazil
  - United Kingdom
  - Russia
  - France
  - Germany
  - South Africa
  - China
  - Kenya
  - Japan
- Handled missing values in critical columns:
  - `total_cases`
  - `new_cases`
  - `total_deaths`
  - `new_deaths`

### 4. Feature Engineering
- Created new metrics such as:
  - Daily case fatality rate
  - Daily case growth rate
  - 7-day rolling averages

### 5. Data Visualization
- Line plots for:
  - Total cases over time
  - New cases per day
  - Total deaths over time
  - Vaccination rollout trends
- Heatmaps for correlation analysis
- Bar plots for comparing countries

---
## Visual Dashboard (desktop): 
https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6


## 📌 Key Insights

- Case surges align with known global COVID-19 waves.
- Vaccination coverage varies widely by country.
- Some countries show a steady decline in deaths following vaccination campaigns.
- Rolling average smoothing improves visibility of trends.

---

## 🧠 Conclusion

This project highlights the power of data analysis in understanding pandemic trends and informing public health decisions. By cleaning and exploring large-scale datasets, we can uncover patterns that help shape policy and response strategies.

---

## 📎 References

- [Our World in Data - COVID-19](https://ourworldindata.org/coronavirus)
- [Johns Hopkins University CSSE](https://github.com/CSSEGISandData/COVID-19)

---

## 📌 Author

**Vanessa Baah-Williams**  
_Exploring real-world data to drive better decisions through analytics._











