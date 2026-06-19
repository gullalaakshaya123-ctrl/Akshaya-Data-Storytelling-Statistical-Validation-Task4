import pandas as pd

# Load dataset
df = pd.read_csv('cleaned_housing_data.csv')

# Statistical summary
print("Dataset Shape:", df.shape)
print("\nDescriptive Statistics:\n", df.describe())

# Correlation analysis
correlation = df.corr(numeric_only=True)
print("\nCorrelation Matrix:\n", correlation)

# Key trends
print("\nAverage Price by Furnishing Status:\n")
print(df.groupby('furnishingstatus')['price'].mean())

print("\nAverage Price by Bedrooms:\n")
print(df.groupby('bedrooms')['price'].mean())