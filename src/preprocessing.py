from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(df):
    df = df.dropna(subset=['Supply Chain Emission Factors with Margins'])

    # Pick columns to use
    features = [
        'Substance', 'Unit',
        'DQ ReliabilityScore of Factors without Margins',
        'DQ TemporalCorrelation of Factors without Margins',
        'DQ GeographicalCorrelation of Factors without Margins',
        'DQ TechnologicalCorrelation of Factors without Margins',
        'DQ DataCollection of Factors without Margins',
        'Source', 'Year'
    ]
    X = df[features]
    y = df['Supply Chain Emission Factors with Margins']

    # Turn text into numbers
    cat_cols = ['Substance', 'Unit', 'Source']
    for col in cat_cols:
        X[col] = LabelEncoder().fit_transform(X[col])

    # Scale numeric values to the same range
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y
