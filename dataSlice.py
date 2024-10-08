import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('processed_dataset_undersampled.csv')  # Replace with your actual dataset file name

# Step 2: Check the number of entries in the dataset
num_entries = len(df)
print(f"Total number of entries in the dataset: {num_entries}")

# Step 3: Determine the number of entries to sample
sample_size = 1000000  # Number of entries to sample

# Ensure sample size does not exceed the number of available entries
if sample_size > num_entries:
    print("Sample size exceeds the total number of entries in the dataset.")
    sample_size = num_entries  # Adjust to sample all available entries

# Step 4: Randomly sample the specified number of entries
sampled_df = df.sample(n=sample_size, random_state=42)

# Step 5: Save the sampled dataset
sampled_df.to_csv('processed_dataset_undersampled_1M.csv', index=False)

print(f"Random sampling completed. {sample_size} entries have been saved as 'processed_dataset_undersampled_1M.csv'.")
