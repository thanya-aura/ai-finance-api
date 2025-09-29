# plus_agent.py - placeholder
import pandas as pd
from typing import Dict


def analyze_plus_margin(df: pd.DataFrame) -> Dict:
    """
    PLUS-tier margin analyzer (under plusd):
    - Computes revenue and margin %
    - Flags low-margin entries (< 20%)
    - Returns concise performance summary
    """

    # ✅ Validate input columns
    required_cols = {"Revenue", "Profit"}
    if not required_cols.issubset(df.columns):
        missing = required_cols - set(df.columns)
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    # ✅ Perform margin calculation
    df["Margin %"] = (df["Profit"] / df["Revenue"]) * 100
    avg_margin = df["Margin %"].mean()

    # ✅ Flag low margin entries
    low_margin_count = df[df["Margin %"] < 20].shape[0]

    return {
        "rows_analyzed": len(df),
        "average_margin_percent": round(avg_margin, 2),
        "low_margin_count": int(low_margin_count),
        "insight": f"{low_margin_count} entries below 20% margin threshold"
    }
