import pandas as pd
import numpy as np


def get_output_schema():
    return pd.DataFrame({
        "Lap_ID": prep_string(),
        "Year": prep_string(),
        "RoundNumber": prep_decimal(),
        "EventName": prep_string(),
        "Driver_Code": prep_string(),
        "Stint": prep_decimal(),
        "Tire_Compound": prep_string(),
        "LapNumber": prep_decimal(),
        "LapTime_Seconds": prep_decimal(),
        "Degradation_Sec": prep_decimal(),
        "LapTime_ZScore": prep_decimal(),
        "Outlier_Lap_Flag": prep_string(),
        "Clean_Lap_For_Model": prep_string()
        
    })


def flag_lap_outliers(df):
    df = df.copy()

    df["LapTime_Seconds"] = pd.to_numeric(df["LapTime_Seconds"], errors="coerce")
    df["Degradation_Sec"] = pd.to_numeric(df["Degradation_Sec"], errors="coerce")

    group_cols = [
        "Year",
        "RoundNumber",
        "EventName",
        "Driver_Code",
        "Stint",
        "Tire_Compound"
    ]

    def safe_zscore(x):
        std = x.std()
        if pd.isna(std) or std == 0:
            return pd.Series(0.0, index=x.index)
        return (x - x.mean()) / std

    df["LapTime_ZScore"] = (
        df.groupby(group_cols)["LapTime_Seconds"]
        .transform(safe_zscore)
    )

    df["Outlier_Lap_Flag"] = np.where(
        df["LapTime_ZScore"].abs() > 2.5,
        "Outlier",
        "Normal"
    )

    df["Clean_Lap_For_Model"] = np.where(
        df["Outlier_Lap_Flag"] == "Outlier",
        "Exclude: Statistical Outlier",
        "Use: Clean Lap"
    )

    return df[[
        "Lap_ID",
        "Year",
        "RoundNumber",
        "EventName",
        "Driver_Code",
        "Stint",
        "Tire_Compound",
        "LapNumber",
        "LapTime_Seconds",
        "Degradation_Sec",
        "LapTime_ZScore",
        "Outlier_Lap_Flag",
        "Clean_Lap_For_Model"
    ]]