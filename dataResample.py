import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('processed_dataset.csv')  # Replace with your actual dataset file name

# Step 2: Check the class distribution
class_counts = df['review_score'].value_counts()
print("Class distribution before undersampling:\n", class_counts)

# Step 3: Separate majority and minority classes
majority_class = df[df['review_score'] == 1]
minority_class = df[df['review_score'] == -1]

# Step 4: Determine the number of entries needed
num_minority = len(minority_class)  # Number of entries in the minority class
num_entries_needed = num_minority * 2  # Total number of entries in the undersampled dataset

# Step 5: Calculate the number of majority class entries to sample
num_majority_to_sample = num_entries_needed - num_minority

# Step 6: Randomly sample from the majority class
undersampled_majority = majority_class.sample(n=num_majority_to_sample, random_state=42)

# Step 7: Combine the sampled majority class with the minority class
undersampled_df = pd.concat([undersampled_majority, minority_class])

# Step 8: Shuffle the final dataset
undersampled_df = undersampled_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Step 9: Save the undersampled dataset
undersampled_df.to_csv('processed_dataset_undersampled_1M.csv', index=False)

print("Undersampling completed. The dataset has been saved as 'processed_dataset_undersampled_1M.csv'.")
