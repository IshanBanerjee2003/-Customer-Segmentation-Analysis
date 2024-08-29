import pandas as pd
from sklearn.cluster import KMeans

# Load processed data
data = pd.read_csv('data/processed/processed_customer_data.csv')

# Perform KMeans clustering
kmeans = KMeans(n_clusters=5, random_state=42)
data['Segment'] = kmeans.fit_predict(data[['Age', 'Income', 'SpendingScore']])

# Save segmented data
data.to_csv('data/processed/segmented_customer_data.csv', index=False)
