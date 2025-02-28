import pandas as pd

def clean_data(df):
    df.dropna(inplace=True)
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna('')
        df[col] = df[col].str.strip().str.lower()
        df['date'] = pd.to_datetime(df['date'])
        df['reviews'] = df['reviews'].str.replace('✅ trip verified |', ' ')
        if df['star rating'] >= 4:
            df['sentiment'] = 'Positive'
        elif df['star rating'] == 3:
            df['sentiment'] = 'Neutral' 
        else:
            df['sentiment'] = 'Negative'
    print("----Data Cleaned----\n")
    print(df.info())
    print(df.isnull().sum())
    return df