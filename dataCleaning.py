import pandas as pd
import re
from bs4 import BeautifulSoup
import cleantext                    
import contractions

def load_stopwords(file_path):
    with open(file_path, 'r') as file:
        stopwords = set(line.strip().lower() for line in file)
    return stopwords

def remove_stopwords(text, stopwords):
    filtered = [word for word in text if word not in stopwords]
    return filtered

def remove_html(text):
    if isinstance(text, str):  # Ensure the input is a string
        return BeautifulSoup(text, "lxml").get_text()
    return ""  # Return an empty string for NaN or non-string values

def preprocess_text(text):

    # remove HTML tags
    text = remove_html(text)

    # remove URLs
    text = re.sub(r'http\S+|https\S+|www\S+', '', text)

    # remove emails
    text = cleantext.clean(text, no_emails=True)

    # remove hashtags
    text = re.sub(r'#\w+', '', text)

    # remove mentions
    text = re.sub(r'@\w+', '', text)

    # remove emoji
    text = cleantext.clean(text, no_emoji=True)

    # lowercase 
    text = text.lower()

    # handle contractions
    text = contractions.fix(text)

    # remove special characters and numbers 
    text = re.sub(r'[^a-z\s]', '', text)

    # remove whitespace
    text = cleantext.clean(text, normalize_whitespace=True)

    # tokenize
    tokens = text.split()

    # remove stopwords
    text = remove_stopwords(tokens, stopwords)

    return text

# global variable for loading stopwords once
stopwords = load_stopwords('stopwords.txt')

# read dataset
dataFrame = pd.read_csv('dataset.csv')

# Remove rows with NaN in 'app_name' or 'review_text'
dataFrame = dataFrame.dropna(subset=['app_name', 'review_text'])

# Drop 'app_id' and 'review_votes' columns
dataFrame = dataFrame.drop(columns=['app_id', 'review_votes'])

# apply preprocessing to 'review_text' column
dataFrame['review_text'] = dataFrame['review_text'].apply(preprocess_text)

# save the cleaned dataset
dataFrame.to_csv('processed_dataset.csv', index=False)

# print the first 10 entries
print(dataFrame.head(10))
