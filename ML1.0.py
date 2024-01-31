import nltk
from nltk.corpus import words
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import random
import string

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
persian_words = set(read_file_as_text('/content/drive/MyDrive/TextPlainDetector/persian_words.txt', ['utf-8', 'windows-1256']).replace('غغغ', ' ').split())

# Read words from the first new dictionary file
file_path1 = '/content/drive/MyDrive/TextPlainDetector/big.txt'  # Replace with the path to your first new dictionary file
new_dictionary_words1 = set(word for word in read_file_as_text(file_path1, ['utf-8', 'windows-1256']).split('\n') if word)

# Read words from the second new dictionary file
file_path2 = '/content/drive/MyDrive/TextPlainDetector/distinct_words.txt'  # Replace with the path to your second new dictionary file
new_dictionary_words2 = set(word for word in read_file_as_text(file_path2, ['utf-8', 'windows-1256']).split('\n') if word)

# Combine English and Persian words into one dictionary
dictionary_words = list(english_words | persian_words | new_dictionary_words1 | new_dictionary_words2)

# Generate random complex strings that are not in the dictionary
random_strings_complex = [''.join(random.choices(string.ascii_letters + string.digits + '!@#$%^&*()_+?|></\*', k=random.randint(1,15))) for _ in range(len(dictionary_words))]
# random_strings_complex = [s for s in random_strings_complex if s not in dictionary_words]

# Generate random simple strings that are not in the dictionary
random_strings_simple = [''.join(random.choices(string.ascii_letters, k=random.randint(1,7))) for _ in range(len(dictionary_words)//2)]
# random_strings_simple = [s for s in random_strings_simple if s not in dictionary_words]


# Define a string of Persian characters
persian_chars = 'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'

# Generate random words
random_strings_persian = [''.join(random.choices(persian_chars, k=random.randint(1,9))) for _ in range(25000)]
random_strings_persian_complex = [''.join(random.choices(persian_chars + string.digits + "!@#$%^&*()_+?\|></", k=random.randint(1,15))) for _ in range(25000)]

# Combine dictionary words and random strings into one list
all_words = dictionary_words + random_strings_complex + random_strings_simple + random_strings_persian + random_strings_persian_complex

# Create labels for the words (True for dictionary words, False for random strings)
labels = [True] * len(dictionary_words) + [False] * len(random_strings_complex) + [False] * len(random_strings_simple) + [False] * len(random_strings_persian)+ [False] * len(random_strings_persian_complex)

# Convert all words to features using CountVectorizer
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(all_words)

# Train a logistic regression model on all words
model = LogisticRegression()
model.fit(features, labels)

# Assume we have a list of file paths
file_paths = ["/content/drive/MyDrive/TextPlainDetector/usf.exe"]  # list of file paths

# Read the texts from the files
texts = [read_file_as_text(file_path, ['utf-8', 'windows-1256', 'latin-1']) for file_path in file_paths]

# Tokenize the text and convert to lower case
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
texts = [tokenizer.tokenize(text.lower())[:50] for text in texts]  # Only take the first 20 words

# Flatten the texts
texts = [word for text in texts for word in text if len(word) >= 2]

# Convert the texts to features using the same vectorizer
features = vectorizer.transform(texts)

# Make predictions on the texts
predictions = model.predict(features)
print(predictions)
# Calculate the percentage of words that are similar to dictionary words
percentage_similar = np.mean(predictions) * 100
print(percentage_similar)
# Print out whether the text is similar to the dictionary words
if percentage_similar >= 95:
    print('The text is similar to the dictionary words.')
else:
    print('The text is not similar to the dictionary words.')


# Get words that are predicted as similar to dictionary words
similar_words = [word for word, pred in zip(texts, predictions) if pred]

print('Words similar to dictionary words:', similar_words)
# from sklearn.externals import joblib

# # Save the model as a pickle file
# joblib.dump(model, 'model.pkl')
# from google.colab import files
# files.download('model.pkl')

import joblib

# Save the vectorizer and the model
joblib.dump((vectorizer, model), 'model_and_vectorizer2.pkl')