import pandas as pd

# Load the data
data = pd.read_csv('data/raw/customer_data.csv')

# Data cleaning and preprocessing
data['DateOfJoining'] = pd.to_datetime(data['DateOfJoining'])
data.dropna(inplace=True)

# Feature engineering
data['CustomerAge'] = 2024 - data['DateOfJoining'].dt.year

# Save processed data
data.to_csv('data/processed/processed_customer_data.csv', index=False)
