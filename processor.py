
import pandas as pd

def analyze_cashflow(df: pd.DataFrame):
    df['Variance'] = df['Actual'] - df['Planned']
    df['Variance %'] = (df['Variance'] / df['Planned']) * 100
    df['Red_Flag'] = df['Variance %'] < -10
    df['Recommendation'] = df.apply(lambda row: (
        "Review spending." if row['Red_Flag'] else
        "Cashflow healthy." if row['Variance'] >= 0 else
        "Monitor closely."), axis=1)
    return df
