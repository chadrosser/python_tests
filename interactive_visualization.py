import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('data/metrics_data.csv')

# Create a bar chart
fig = px.bar(df, x='Metric A', y='Metric B', title='Metrics Overview')

# Show the plot
fig.show()
