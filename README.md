# F1 Tire Degradation Analysis

## Project Overview

This project analyzes Formula 1 tire degradation using race lap data, race result data, and weather data. The complete data preparation workflow was built in **Tableau Prep Builder**, while advanced calculations such as outlier detection and tire degradation trend analysis were performed using **Python through TabPy**.

The main goal of the project is to create a clean, model-ready dataset that helps understand how lap performance changes across stints, tire compounds, race conditions, and weather factors. The workflow prepares the data for further analysis, visualization, and decision-making related to Formula 1 tire strategy.

## Problem Statement

In Formula 1, tire degradation has a major impact on lap time, race pace, and pit-stop strategy. As tires wear out during a stint, lap times may increase, and teams need to decide when the tire performance drop becomes risky.

This project focuses on answering questions such as:

- How does lap time change during a tire stint?
- Which laps show abnormal lap-time behavior?
- How can outlier laps be identified and removed from the model-ready dataset?
- How can rolling tire degradation be calculated?
- Which tire stints show low, medium, or high pit risk?
- How can weather and race result data improve tire degradation analysis?

## Tools and Technologies Used

- **Tableau Prep Builder** – for data cleaning, joining, aggregation, transformation, and workflow creation
- **TabPy** – for running Python scripts inside Tableau Prep
- **Python** – for advanced calculations and custom logic
- **Pandas** – for data manipulation
- **NumPy** – for numerical calculations
- **FastF1** – for extracting Formula 1 session data
- **GitHub** – for version control and project documentation

## Repository Structure

```text
F1-Tire-Degradation/
│
├── Dataset/
│   ├── tire_data_2025
│   ├── race_2025
│   └── weather_2025
│
├── output/
│   └── Final cleaned / model-ready outputs
│
├── Final_Flow.tfl
│   └── Tableau Prep Builder flow file
│
├── Python_Outlier_Detection.py
│   └── TabPy script for identifying outlier laps
│
├── Python_Degradation_Trend.py
│   └── TabPy script for calculating rolling degradation and pit risk
│
├── main.py
│   └── FastF1 data extraction script
│
├── LICENSE
│
└── README.md
```

## Dataset Description

The project uses three main datasets:

### 1. Tire Data
Contains lap-level tire and stint information, such as:

- Driver
- Lap number
- Stint number
- Tire compound
- Lap time
- Tire-related performance indicators

### 2. Race Results Data
Contains race-level result information, such as:

- Race year
- Round number
- Event name
- Driver result details
- Finishing position or race outcome information

### 3. Weather Data
Contains race weather conditions, such as:

- Air temperature
- Track temperature
- Humidity
- Rainfall or weather conditions
- Session timing information

These datasets are joined together in Tableau Prep to create a complete analytical dataset for tire degradation analysis.

## Workflow Explanation

The complete workflow was created in **Tableau Prep Builder**. The flow combines cleaning, joining, aggregation, Python scripting, and final output generation.

### 1. Data Input

The workflow starts with three input sources:

- `tire_data_2025`
- `race_2025`
- `weather_2025`

These datasets provide the base information for tire, race, and weather analysis.

### 2. Data Profiling and Cleaning

The tire data is first passed through a profiling and cleaning step. This helps identify and fix issues such as:

- Incorrect data types
- Missing values
- Unwanted columns
- Inconsistent formats
- Invalid lap or stint records

The weather data is also aggregated and cleaned before it is joined with the race and tire data.

### 3. Joining Race and Tire Data

The race data is joined with the tire data to connect tire performance with race context. This allows each lap record to include event and driver-level information.

### 4. Joining Weather Data

The cleaned weather data is joined with the race-tire dataset. This step adds environmental context to the tire degradation analysis.

Weather is important because track temperature, air temperature, and conditions can influence tire performance and degradation.

### 5. Stint-Level Aggregations

The workflow calculates stint-level metrics, including:

- Average stint lap
- Best stint lap
- Stint-level lap-time comparison

These aggregated values help compare each lap against the overall performance of the stint.

### 6. Calculating Tire Degradation

A calculated step is used to estimate tire degradation. The degradation value represents the lap-time performance drop compared with a reference lap or stint benchmark.

A simple interpretation is:

```text
Higher degradation value = larger lap-time loss = worse tire performance
```

### 7. Python Outlier Detection using TabPy

The workflow uses `Python_Outlier_Detection.py` through TabPy to identify abnormal laps.

The script:

- Groups laps by year, round, event, driver, stint, and tire compound
- Calculates a lap-time z-score
- Flags laps with extreme z-score values as outliers
- Creates a clean-lap flag for model preparation

Main output fields from this script include:

- `LapTime_ZScore`
- `Outlier_Lap_Flag`
- `Clean_Lap_For_Model`

Outlier logic:

```text
If absolute LapTime_ZScore > 2.5 → Outlier
Otherwise → Normal
```

This helps remove laps affected by unusual events such as mistakes, traffic, safety cars, pit entry/exit effects, or abnormal lap behavior.

### 8. Python Degradation Trend Analysis using TabPy

The workflow also uses `Python_Degradation_Trend.py` to calculate tire degradation trend values.

The script:

- Sorts laps by race, driver, stint, and lap number
- Calculates a rolling 3-lap average degradation
- Classifies the stint into pit-risk levels

Main output fields from this script include:

- `Rolling_3Lap_Degradation`
- `Python_Pit_Risk_Level`

Pit risk logic:

```text
Rolling_3Lap_Degradation >= 1.5 → High Risk
Rolling_3Lap_Degradation >= 1.0 → Medium Risk
Rolling_3Lap_Degradation < 1.0  → Low Risk
```

This gives a simple strategy indicator for understanding when tire performance is becoming risky.

### 9. Final Join and Output

After Python processing, the results are joined back into the main Tableau Prep flow. The final model-ready dataset is then exported as the project output.

The final output can be used for:

- Tableau dashboards
- Tire strategy analysis
- Driver performance comparison
- Compound performance comparison
- Pit-risk analysis
- Further machine learning or predictive modeling

## Key Features of the Project

- End-to-end data preparation workflow in Tableau Prep Builder
- Multiple datasets joined into one final analytical dataset
- Weather data integrated with race and tire data
- Stint-level lap performance analysis
- Python-based outlier detection using z-score
- Rolling 3-lap degradation calculation
- Pit-risk classification using Python logic
- Final cleaned and model-ready output generation

## Python Scripts

### `main.py`

This script uses FastF1 to load Formula 1 session data and export CSV files.

It extracts:

- Lap data
- Race results
- Weather data

Example output files:

```text
output/laps.csv
output/results.csv
output/weather.csv
```

### `Python_Outlier_Detection.py`

This script is used inside Tableau Prep through TabPy.

Purpose:

- Detect abnormal lap times
- Calculate lap-time z-scores
- Flag outlier laps
- Mark whether a lap should be used for modeling

### `Python_Degradation_Trend.py`

This script is also used inside Tableau Prep through TabPy.

Purpose:

- Calculate rolling 3-lap degradation
- Create tire performance trend indicators
- Assign pit-risk levels

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/yuvrajghag5/F1-Tire-Degradation.git
cd F1-Tire-Degradation
```

### Step 2: Install Python Dependencies

```bash
pip install pandas numpy fastf1 tabpy
```

### Step 3: Start TabPy

```bash
tabpy
```

Keep TabPy running while working with the Tableau Prep flow.

### Step 4: Open Tableau Prep Builder

Open the Tableau Prep flow file:

```text
Final_Flow.tfl
```

### Step 5: Configure TabPy in Tableau Prep

In Tableau Prep Builder:

1. Go to **Help** or **Server** settings depending on your Tableau Prep version
2. Open **External Service Connection**
3. Select **TabPy**
4. Use the default local server settings:

```text
Host: localhost
Port: 9004
```

### Step 6: Run the Flow

Run the full Tableau Prep workflow to generate the final output.

## Final Output

The final output contains cleaned, enriched, and model-ready F1 tire degradation data.

Important final columns include:

- `Lap_ID`
- `Year`
- `RoundNumber`
- `EventName`
- `Driver_Code`
- `Stint`
- `Tire_Compound`
- `LapNumber`
- `LapTime_Seconds`
- `Degradation_Sec`
- `LapTime_ZScore`
- `Outlier_Lap_Flag`
- `Clean_Lap_For_Model`
- `Rolling_3Lap_Degradation`
- `Python_Pit_Risk_Level`

## Possible Analysis Questions

This dataset can be used to answer:

- Which tire compound degrades fastest?
- Which drivers manage tires better across a stint?
- How does weather affect lap-time degradation?
- Which laps should be excluded as statistical outliers?
- When does a stint move from low risk to medium or high pit risk?
- How does tire degradation differ across races or circuits?

## Project Outcome

The project successfully creates a full data preparation and analysis pipeline for Formula 1 tire degradation. By combining Tableau Prep Builder with Python and TabPy, the workflow handles both visual data preparation and advanced analytical calculations.

The final dataset is useful for understanding race strategy, tire behavior, lap-time consistency, and pit-stop risk.

## Author

**Yuvraj Ghag**  
GitHub: [@yuvrajghag5](https://github.com/yuvrajghag5)

## License

This project is licensed under the MIT License.
