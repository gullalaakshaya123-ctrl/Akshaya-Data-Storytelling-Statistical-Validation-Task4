import pandas as pd
from scipy.stats import ttest_ind

# Load dataset
df = pd.read_csv('cleaned_housing_data.csv')

# Hypothesis:
# H0: Furnished and Unfurnished house prices have no significant difference
# H1: Significant price difference exists

furnished = df[df['furnishingstatus'] == 'Furnished']['price']
unfurnished = df[df['furnishingstatus'] == 'Unfurnished']['price']

# T-test
t_stat, p_value = ttest_ind(furnished, unfurnished, nan_policy='omit')

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Reject Null Hypothesis: Significant difference exists.")
else:
    print("Fail to Reject Null Hypothesis: No significant difference.")