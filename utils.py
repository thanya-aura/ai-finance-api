def analyze_cashflow(df):
    df['Variance'] = df['Actual'] - df['Planned']
    df['Red_Flag'] = df['Variance'] < -0.1 * df['Planned']
    return df.to_dict(orient='records')