import nltk
from nltk.corpus import words
from nltk.tokenize import word_tokenize
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import nltk
nltk.download('punkt')
# Load English dictionary
nltk.download('words')
english_words = set(words.words())

def load_dictionary(dictionary_path):
    encodings = ['utf-8', 'windows-1256']
    dictionary_words = []
    for encoding in encodings:
        try:
            with open(dictionary_path, 'r', encoding=encoding) as f:
                dictionary_words = set(word.replace('غغغ', ' ').rstrip() for word in f.read().splitlines())
            break
        except UnicodeDecodeError:
            continue
    return dictionary_words

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception:
        return ''
    return text

def check_text(text, dictionary_words):
    tokens = word_tokenize(text)
    meaningful_words = [word for word in tokens if word in english_words or word in dictionary_words]
    return 'meaningful' if len(meaningful_words) >= len(tokens) * 0.1 else 'not meaningful'

# Load Persian dictionary
persian_words = load_dictionary('english-text.txt')

# Read file
file_path = "farsi-text.txt"  # Replace with your file path
text = read_file(file_path)

# Check if the text is meaningful
print('Prediction:', check_text(text, persian_words))
