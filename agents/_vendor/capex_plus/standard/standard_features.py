def calculate_variance(df):
    df["Variance"] = df["Planned"] - df["Actual"]
    return df
