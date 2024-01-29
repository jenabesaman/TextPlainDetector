import nltk
from nltk.corpus import words as nltk_words
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_dictionary(dictionary_path):
    encodings = ['utf-8', 'windows-1256']
    dictionary_words = []
    for encoding in encodings:
        try:
            with open(dictionary_path, 'r', encoding=encoding, errors='ignore') as f:
                dictionary_words = set(word.replace('غغغ', ' ').rstrip() for word in f.read().splitlines())
            break
        except UnicodeDecodeError:
            continue
    return dictionary_words

def check_persian_words(file_path, dictionary_path):
    encodings = ['utf-8', 'windows-1256']

    dictionary_words = load_dictionary(dictionary_path)

    file_words = []
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                file_words = f.read().replace('غغغ', ' ').split()
            break
        except UnicodeDecodeError:
            continue

    if not file_words:
        print(f"Failed to open file with encodings: {encodings}")
        return

    return file_words, dictionary_words

# Load the dictionaries
file_path = "farsi-text.txt"  # Replace with your file path
dictionary_path = 'persian_words.txt'  # Replace with your dictionary path
words, all_words = check_persian_words(file_path, dictionary_path)
english_words = set(nltk_words.words())
all_words = all_words.union(english_words)

# Create a TF-IDF vectorizer and fit it to the combined data
combined = list(all_words) + words
vectorizer = TfidfVectorizer().fit(combined)

# Transform the dictionary and words into TF-IDF vectors
dictionary_vector = vectorizer.transform(list(all_words))
words_vector = vectorizer.transform(words)

# Calculate the cosine similarity between each word and the dictionary
similarities = cosine_similarity(words_vector, dictionary_vector)

# Determine if each word is similar to any dictionary word
threshold = 0.0  # Set your threshold here
is_similar = (similarities.max(axis=1) > threshold).tolist()

# Determine if the text is meaningful
is_meaningful = any(is_similar)
print(is_meaningful)
