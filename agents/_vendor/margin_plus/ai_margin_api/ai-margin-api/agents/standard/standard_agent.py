# standard_agent.py - placeholder
import pandas as pd
from typing import Dict


def analyze_standard_margin(df: pd.DataFrame) -> Dict:
    """
    Standard-tier margin analyzer:
    - Calculates basic revenue, profit, and margin %
    - Returns simple summary stats
    """
    # ✅ Check for required columns
    required_cols = {"Revenue", "Profit"}
    if not required_cols.issubset(df.columns):
        missing = required_cols - set(df.columns)
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    # ✅ Compute margin %
    df["Margin %"] = (df["Profit"] / df["Revenue"]) * 100

    # ✅ Compute basic summary
    total_revenue = df["Revenue"].sum()
    total_profit = df["Profit"].sum()
    avg_margin = df["Margin %"].mean()

    return {
        "total_revenue": round(total_revenue, 2),
        "total_profit": round(total_profit, 2),
        "average_margin_percent": round(avg_margin, 2),
        "message": "Standard margin analysis completed."
    }
