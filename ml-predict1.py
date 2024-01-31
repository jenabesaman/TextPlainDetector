import nltk
import joblib
import numpy as np
# from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
# vectorizer = CountVectorizer()
# Load the model from the pickle file
# Load the vectorizer and the model
vectorizer, model = joblib.load('model_and_vectorizer.pkl')

# Assume we have a list of file paths
file_paths = ["farsi-text.txt"]  # list of file paths

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

# Read the texts from the files
texts = [read_file_as_text(file_path, ['utf-8', 'windows-1256', 'latin-1']) for file_path in file_paths]
print(texts)

# Tokenize the text and convert to lower case
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
texts = [tokenizer.tokenize(text.lower())[:50] for text in texts]  # Only take the first 20 words

# Flatten the texts
texts = [word for text in texts for word in text]

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