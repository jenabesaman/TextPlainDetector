import nltk
from nltk.corpus import words
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Download the words corpus if you haven't done so already
nltk.download('words')

# This is your dictionary of English words
english_words = set(words.words())

# Function to read text from a file with different encodings
def read_file_as_text(file_path, encodings):
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            pass
    # If the provided encodings fail, try 'latin-1'
    try:
        with open(file_path, 'rb') as file:
            return file.read().decode('latin-1')
    except UnicodeDecodeError:
        print(f'Could not read {file_path} with any of the provided encodings.')
        return ''

# Read your Persian dictionary from a file
persian_words = set(read_file_as_text('persian_words.txt', ['utf-8', 'windows-1256']).replace('غغغ', ' ').split())

# Combine English and Persian words into one dictionary
dictionary_words = list(english_words | persian_words)

# Convert dictionary words to features using CountVectorizer
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(dictionary_words)

# Create labels for the dictionary words (all True because all dictionary words are in the dictionary)
labels = [True] * len(dictionary_words)

# Train a logistic regression model on the dictionary words
model = LogisticRegression()
model.fit(features, labels)

# Assume we have a list of file paths
file_paths = ["farsi-text.txt"]  # list of file paths

# Read the texts from the files
texts = [read_file_as_text(file_path, ['utf-8', 'windows-1256', 'latin-1']) for file_path in file_paths]

# Tokenize the text and convert to lower case
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
texts = [tokenizer.tokenize(text.lower())[:20] for text in texts]  # Only take the first 20 words

# Flatten the texts
texts = [word for text in texts for word in text]

# Convert the texts to features using the same vectorizer
features = vectorizer.transform(texts)

# Make predictions on the texts
predictions = model.predict(features)

# Calculate the percentage of words that are similar to dictionary words
percentage_similar = np.mean(predictions) * 100

# Print out whether the text is similar to the dictionary words
if percentage_similar >= 70:
    print('The text is similar to the dictionary words.')
else:
    print('The text is not similar to the dictionary words.')
