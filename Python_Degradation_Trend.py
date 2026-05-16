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
        "Clean_Lap_For_Model": prep_string(),
        "Rolling_3Lap_Degradation": prep_decimal(),
        "Python_Pit_Risk_Level": prep_string()
    })


def calculate_degradation_trend(df):
    df = df.copy()

    df["LapNumber"] = pd.to_numeric(df["LapNumber"], errors="coerce")
    df["Degradation_Sec"] = pd.to_numeric(df["Degradation_Sec"], errors="coerce")

    group_cols = [
        "Year",
        "RoundNumber",
        "EventName",
        "Driver_Code",
        "Stint",
        "Tire_Compound"
    ]

    sort_cols = [
        "Year",
        "RoundNumber",
        "EventName",
        "Driver_Code",
        "Stint",
        "LapNumber"
    ]

    df = df.sort_values(sort_cols)

    df["Rolling_3Lap_Degradation"] = (
        df.groupby(group_cols)["Degradation_Sec"]
        .transform(lambda x: x.rolling(window=3, min_periods=1).mean())
    )

    df["Python_Pit_Risk_Level"] = np.where(
        df["Rolling_3Lap_Degradation"] >= 1.5,
        "High Risk",
        np.where(
            df["Rolling_3Lap_Degradation"] >= 1.0,
            "Medium Risk",
            "Low Risk"
        )
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
        "Clean_Lap_For_Model",
        "Rolling_3Lap_Degradation",
        "Python_Pit_Risk_Level"
    ]]