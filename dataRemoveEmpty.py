import pandas as pd

# Read the dataset
dataFrame = pd.read_csv('processed_dataset.csv')

# Remove rows where 'review_text' is exactly "[]"
dataFrame = dataFrame[dataFrame['review_text'] != "[]"]

# Save the cleaned dataset
dataFrame.to_csv('cleaned_dataset.csv', index=False)

# Print the first 10 entries of the cleaned dataset
print(dataFrame.head(10))
