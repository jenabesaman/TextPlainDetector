import nltk
from nltk.corpus import words
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

# Download the words corpus if you haven't done so already
nltk.download('words')

# This is your dictionary of English words
english_words = set(words.words())

def read_file_as_text(file_path, encodings):
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            pass
    print(f'Could not read {file_path} with any of the provided encodings.')
    return ''


# Read your Persian dictionary from a file
persian_words = set(read_file_as_text('persian_words.txt', ['utf-8', 'windows-1256',"latin-1"]).replace('غغغ', ' ').split())

# Combine English and Persian words into one dictionary
dictionary_words = english_words | persian_words

# Function to calculate Jaccard similarity
def jaccard_similarity(word1, word2):
    set1 = set(word1)
    set2 = set(word2)
    return len(set1 & set2) / len(set1 | set2)

# Assume we have a list of file paths
file_paths = ["farsi-text.txt"]  # list of file paths

# Read the texts from the files
texts = [read_file_as_text(file_path, ['utf-8', 'windows-1256']) for file_path in file_paths]

# Tokenize the text and convert to lower case
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
texts = [tokenizer.tokenize(text.lower())[:50] for text in texts]  # Only take the first 20 words

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

# # Make predictions on the test set
# predictions = model.predict(features_test)
# print(predictions)

import numpy as np

predictions = np.array(predictions)
print('Number of True predictions:', np.sum(predictions))
print('Number of False predictions:', len(predictions) - np.sum(predictions))
