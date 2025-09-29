import pandas as pd
from typing import Dict


def analyze_premium_margin(df: pd.DataFrame) -> Dict:
    """
    Premium-tier margin analyzer:
    - Extracts KPIs: Revenue, Profit, Margin %
    - Flags red flags on low margin or high variance
    - Returns SOX controls placeholder and forecast summary
    """

    # ✅ Validate required columns
    required_columns = {"Revenue", "Profit"}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    # ✅ Calculate derived metrics
    df["Margin %"] = (df["Profit"] / df["Revenue"]) * 100
    df["Variance"] = df["Revenue"] - df["Profit"]

    # ✅ Red flag detection logic
    red_flags = []
    if (df["Margin %"] < 15).any():
        red_flags.append("❗ Some margin percentages are below 15% threshold.")
    if (df["Variance"] > df["Revenue"] * 0.5).any():
        red_flags.append("⚠️ Variance exceeds 50% of revenue in some entries.")

    # ✅ Summary metrics
    avg_margin = df["Margin %"].mean()
    avg_variance = df["Variance"].mean()

    # ✅ Simulated SOX controls status
    sox_status = "✅ Controls in place" if avg_margin >= 25 else "❌ Controls review recommended"

    # ✅ Forecast summary generation
    if avg_margin >= 30:
        forecast_note = "📈 Strong forecast outlook with healthy margins."
    elif avg_margin >= 20:
        forecast_note = "📊 Forecast stable but margin optimization needed."
    else:
        forecast_note = "📉 Forecast weak—investigate profitability and cost base."

    return {
        "rows_analyzed": len(df),
        "average_margin_percent": round(avg_margin, 2),
        "average_variance": round(avg_variance, 2),
        "red_flags": red_flags,
        "sox_controls_status": sox_status,
        "forecast_summary": forecast_note
    }
