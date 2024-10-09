import pandas as pd

# Read the dataset
dataFrame = pd.read_csv('cleaned_dataset.csv')

# Remove rows where 'review_text' is exactly "[]"
dataFrame = dataFrame[dataFrame['review_text'] != "['early', 'access', 'review']"]

# Save the cleaned dataset
dataFrame.to_csv('cleaned_dataset_no_EAR.csv', index=False)

