import pandas as pd

# Function to split the dataset based on review_score
def split_reviews(input_csv):
    # Read the dataset from the input CSV file
    data = pd.read_csv(input_csv)

    # Check if 'review_score' column exists
    if 'review_score' not in data.columns:
        raise ValueError("The 'review_score' column is not found in the dataset.")

    # Split the dataset into two based on review_score
    positive_reviews = data[data['review_score'] == 1]
    negative_reviews = data[data['review_score'] == -1]

    # Save the split datasets into separate CSV files
    positive_reviews.to_csv('positive_reviews.csv', index=False)
    negative_reviews.to_csv('negative_reviews.csv', index=False)

    print("Data split into 'positive_reviews.csv' and 'negative_reviews.csv'.")

# Example usage
if __name__ == "__main__":
    input_csv = 'cleaned_dataset_no_EAR_undersampled_1M.csv'  # Replace with your input CSV file name
    split_reviews(input_csv)
