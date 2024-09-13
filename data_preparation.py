import pandas as pd

# Simulated data
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
    'Metric A': [95, 85, 88, 92],
    'Metric B': [77, 85, 80, 70],
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('data/metrics_data.csv', index=False)
