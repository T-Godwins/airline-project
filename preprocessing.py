import pandas as pd
from nltk.corpus import stopwords
import nltk

def clean_data(df):
    """Clean and preprocess the data"""
    # Create a copy to avoid modifying the original dataframe
    df = df.copy()
    
    # Handle string columns
    for col in df.select_dtypes(include=['object']).columns:
        # Convert to string first, then apply string operations
        df[col] = df[col].fillna('')
        df[col] = df[col].astype(str).str.strip().str.lower()
    
    # Convert date
    df['date'] = pd.to_datetime(df['date'])
    
    # Clean reviews - keep sentences intact for sentence transformers
    df['reviews'] = df['reviews'].str.replace('✅ trip verified |', ' ', regex=False)
    
    # Create sentiment categories
    df['sentiment'] = pd.cut(
        df['star rating'],
        bins=[-float('inf'), 4, 6, float('inf')],
        labels=['Negative', 'Neutral', 'Positive']
    )
    
    print("----Data Cleaned----\n")
    print(df.info())
    print("\nNull values:\n", df.isnull().sum())
    print("\nSentiment distribution:\n", df['sentiment'].value_counts())
    
    return df