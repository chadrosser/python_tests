import pandas as pd

# Load data
df = pd.read_csv('data/metrics_data.csv')

# Calculate basic statistics
def calculate_metrics(dataframe):
    metrics = {
        'Mean Metric A': dataframe['Metric A'].mean(),
        'Mean Metric B': dataframe['Metric B'].mean(),
        'Standard Deviation Metric A': dataframe['Metric A'].std(),
        'Standard Deviation Metric B': dataframe['Metric B'].std(),
    }
    return metrics

# Calculate metrics
metrics = calculate_metrics(df)

# Print metrics
for metric, value in metrics.items():
    print(f'{metric}: {value}')
