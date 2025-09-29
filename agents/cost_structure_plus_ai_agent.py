def analyze(df):
    return {
        "agent": "plus",
        "total_cost": df["Cost"].sum(),
        "avg_unit_margin": df["Unit Margin"].mean()
    }