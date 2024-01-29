import nltk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

# Function to read text from a file with different encodings
def read_file(file_path, encodings):
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            pass
    print(f'Could not read {file_path} with any of the provided encodings.')
    return ''

# Read your Persian dictionary from a file
dictionary_words = set(read_file('persian-word.txt', ['utf-8', 'windows-1256']).replace('غغغ', ' ').split())

# Function to calculate Jaccard similarity
def jaccard_similarity(word1, word2):
    set1 = set(word1)
    set2 = set(word2)
    return len(set1 & set2) / len(set1 | set2)

# Assume we have a list of file paths
file_paths = [...]  # list of file paths

# Read the texts from the files
texts = [read_file(file_path, ['utf-8', 'windows-1256']) for file_path in file_paths]

# Tokenize the text and convert to lower case
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
texts = [tokenizer.tokenize(text.lower()) for text in texts]

# Create binary labels for whether each word is similar to a dictionary word
labels = [[any(jaccard_similarity(word, dict_word) >= 0.7 for dict_word in dictionary_words) for word in text] for text in texts]

# Flatten texts and labels
texts = [word for text in texts for word in text]
labels = [label for sublist in labels for label in sublist]

# Convert texts to features using CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(texts)

# Split the data into training and test sets
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(features_train, labels_train)

# Make predictions on the test set
predictions = model.predict(features_test)
