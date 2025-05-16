# COVID-19 Global Data Tracker
# =====================================================

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

# Set style for visualizations
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Set2")
plt.rcParams['figure.figsize'] = [12, 7]
plt.rcParams['figure.dpi'] = 100

# Data Collection
print("1. LOADING COVID-19 DATA")
print("=" * 50)

# Load data from Our World in Data COVID-19 dataset
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
print(f"Loading data from: {url}")

try:
    df = pd.read_csv(url)
    print(f"Data loaded successfully! Shape: {df.shape}")
except Exception as e:
    print(f"Error loading data: {e}")
    print("Please download the dataset manually from https://covid.ourworldindata.org/data/owid-covid-data.csv")
    exit(1)

# 2️⃣ Data Loading & Exploration
# =====================================================
print("\n2. DATA EXPLORATION")
print("=" * 50)

# Display basic information about the dataset
print("\nColumns in the dataset:")
print(df.columns.tolist())

print("\nFirst few rows of the dataset:")
print(df.head())

print("\nBasic information about the dataset:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

print("\nMissing values in each column:")
print(df.isnull().sum())

# Check for continents vs countries
print("\nUnique locations in the dataset:")
unique_locations = df['location'].unique()
print(f"Total unique locations: {len(unique_locations)}")
print(f"Sample locations: {unique_locations[:10]}")

# 3️⃣ Data Cleaning
# =====================================================
print("\n3. DATA CLEANING")
print("=" * 50)

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])
print("Converted 'date' column to datetime format")

# Check for continents and special entities
continents = ['World', 'Europe', 'North America', 'South America', 
              'Asia', 'Africa', 'Oceania', 'European Union']
print(f"\nRemoving aggregated data for: {continents}")
df_countries = df[~df['location'].isin(continents)]
print(f"Remaining rows after removing continents: {df_countries.shape[0]}")

# Select countries of interest
countries_of_interest = ['United States', 'India', 'Brazil', 'United Kingdom', 
                        'Russia', 'France', 'Germany', 'South Africa', 
                        'China', 'Kenya', 'Japan']
print(f"\nSelecting data for countries: {countries_of_interest}")
df_selected = df[df['location'].isin(countries_of_interest)]
print(f"Selected data shape: {df_selected.shape}")

# Basic cleaning: Handle missing values for key metrics
key_metrics = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths']
print(f"\nHandling missing values for key metrics: {key_metrics}")
for metric in key_metrics:
    # Replace missing values with 0
    missing_before = df_selected[metric].isnull().sum()
    df_selected[metric] = df_selected[metric].fillna(0)
    print(f"Filled {missing_before} missing values in '{metric}' with 0")

# Calculate additional metrics
print("\nCalculating additional metrics...")
# Calculate death rate (mortality rate)
df_selected['death_rate'] = (df_selected['total_deaths'] / df_selected['total_cases'] * 100).round(2)
print("Added 'death_rate' column (total_deaths / total_cases * 100)")

print("\nCleaned dataset preview:")
print(df_selected.head())

# 4️⃣ Exploratory Data Analysis (EDA)
# =====================================================
print("\n4. EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# Get the latest data for each country
latest_date = df_selected['date'].max()
print(f"\nLatest date in the dataset: {latest_date}")

latest_data = df_selected[df_selected['date'] == latest_date]
print("\nLatest COVID-19 statistics by country:")
latest_summary = latest_data[['location', 'total_cases', 'total_deaths', 'death_rate']].sort_values('total_cases', ascending=False)
print(latest_summary)

# Plot total cases over time for selected countries
print("\nPlotting total cases over time for selected countries...")
plt.figure(figsize=(14, 8))
for country in countries_of_interest:
    country_data = df_selected[df_selected['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Cases', fontsize=12)
plt.yscale('log')  # Using log scale for better visualization
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('total_cases_over_time.png')
plt.close()
print("Plot saved as 'total_cases_over_time.png'")

# Plot total deaths over time
print("\nPlotting total deaths over time for selected countries...")
plt.figure(figsize=(14, 8))
for country in countries_of_interest:
    country_data = df_selected[df_selected['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
plt.title('Total COVID-19 Deaths Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Deaths', fontsize=12)
plt.yscale('log')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('total_deaths_over_time.png')
plt.close()
print("Plot saved as 'total_deaths_over_time.png'")

# Compare daily new cases
print("\nComparing daily new cases (7-day rolling average)...")
plt.figure(figsize=(14, 8))
for country in countries_of_interest:
    country_data = df_selected[df_selected['location'] == country]
    # Calculate 7-day rolling average for smoother visualization
    rolling_avg = country_data['new_cases'].rolling(window=7).mean()
    plt.plot(country_data['date'], rolling_avg, label=country)
plt.title('Daily New COVID-19 Cases (7-day Rolling Average)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('New Cases (7-day Avg)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('new_cases_rolling_avg.png')
plt.close()
print("Plot saved as 'new_cases_rolling_avg.png'")

# Bar chart: Top countries by total cases
print("\nCreating bar chart of total cases by country...")
plt.figure(figsize=(14, 8))
sns.barplot(x='location', y='total_cases', data=latest_summary)
plt.title('Total COVID-19 Cases by Country (Latest Data)', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Total Cases', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('total_cases_by_country.png')
plt.close()
print("Plot saved as 'total_cases_by_country.png'")

# 5️⃣ Visualizing Vaccination Progress
# =====================================================
print("\n5. VACCINATION PROGRESS ANALYSIS")
print("=" * 50)

# Check if vaccination data is available
if 'people_fully_vaccinated_per_hundred' in df_selected.columns:
    print("\nAnalyzing vaccination data...")
    
    # Plot vaccination progress for selected countries
    plt.figure(figsize=(14, 8))
    for country in countries_of_interest:
        country_data = df_selected[df_selected['location'] == country]
        # Some countries might have NaN for vaccination data
        plt.plot(country_data['date'], country_data['people_fully_vaccinated_per_hundred'], label=country)
    plt.title('Percentage of Population Fully Vaccinated Against COVID-19', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Percentage of Population', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('vaccination_progress.png')
    plt.close()
    print("Plot saved as 'vaccination_progress.png'")
    
    # Latest vaccination data by country
    latest_vax = latest_data[['location', 'people_fully_vaccinated_per_hundred']].sort_values('people_fully_vaccinated_per_hundred', ascending=False)
    print("\nLatest vaccination percentages by country:")
    print(latest_vax)
    
    # Bar chart of vaccination percentages
    plt.figure(figsize=(14, 8))
    sns.barplot(x='location', y='people_fully_vaccinated_per_hundred', data=latest_vax)
    plt.title('Percentage of Population Fully Vaccinated (Latest Data)', fontsize=16)
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Percentage of Population', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('vaccination_percentage_by_country.png')
    plt.close()
    print("Plot saved as 'vaccination_percentage_by_country.png'")
else:
    print("\nVaccination data not available in the dataset")

# 6️⃣ Choropleth Map Visualization
# =====================================================
print("\n6. CHOROPLETH MAP VISUALIZATION")
print("=" * 50)

# Create a choropleth map showing total cases per million people
print("\nCreating choropleth map of total cases per million people...")

# For this to work, we need the complete dataset with all countries
all_countries_latest = df[df['date'] == latest_date]

# Check if we have the required columns
if 'iso_code' in all_countries_latest.columns and 'total_cases_per_million' in all_countries_latest.columns:
    try:
        # Create map using plotly
        fig = px.choropleth(all_countries_latest, 
                           locations="iso_code",
                           color="total_cases_per_million", 
                           hover_name="location",
                           color_continuous_scale=px.colors.sequential.Plasma,
                           title="COVID-19 Total Cases per Million People (Global View)")
        
        fig.update_layout(
            coloraxis_colorbar=dict(title="Cases per Million"),
            title=dict(font=dict(size=20)),
            geo=dict(showframe=False, showcoastlines=True)
        )
        
        # Save as an HTML file
        fig.write_html("covid_cases_map.html")
        print("Interactive map saved as 'covid_cases_map.html'")
    except Exception as e:
        print(f"Error creating choropleth map: {e}")
else:
    print("Required columns for choropleth map not available in the dataset")

# 7️⃣ Insights & Reporting
# =====================================================
print("\n7. KEY INSIGHTS FROM THE ANALYSIS")
print("=" * 50)

print("""
Key Insights from COVID-19 Global Data Analysis:

1. Case Distribution: The data shows significant variation in COVID-19 case numbers 
   across countries, with some nations experiencing much higher case loads than others.
   The United States, India, and Brazil have consistently reported the highest
   total case numbers.

2. Mortality Rates: Death rates (calculated as total deaths divided by total cases)
   vary significantly between countries, potentially reflecting differences in
   healthcare systems, reporting methodologies, testing capacity, and population 
   demographics.

3. Vaccination Progress: There are substantial disparities in vaccination rates
   globally. Some countries have achieved high vaccination percentages while
   others lag behind significantly.

4. Wave Patterns: The analysis of daily new cases reveals distinct "wave" patterns
   across different countries, with peaks and valleys occurring at different times,
   reflecting the regional nature of outbreaks and varying effectiveness of
   containment measures.

5. Testing Influence: Variations in testing capacity and strategies between
   countries likely impact reported case numbers, making direct comparisons
   challenging. Countries with more robust testing infrastructures may report
   higher case numbers.
""")

print("""
Conclusions and Recommendations:

1. Continued vigilance and public health measures remain important, particularly
   in regions with low vaccination rates.

2. International cooperation on vaccine distribution could help address the
   significant disparities in vaccination coverage.

3. Standardized reporting methodologies would improve the comparability of
   data across countries.

4. For future pandemic preparedness, investing in robust testing infrastructure
   and early warning systems is crucial.

5. Regular monitoring of emerging variants and their potential impact on
   case trajectories should be prioritized.
""")

print("\nAnalysis completed successfully!")