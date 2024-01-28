import nltk
from nltk.corpus import words

# Download the word list if not already downloaded
nltk.download('words')

def detect_meaning(file_path, dictionary_path):
    encodings = ['utf-8', 'windows-1256']

    dictionary_words = []
    for encoding in encodings:
        try:
            with open(dictionary_path, 'r', encoding=encoding) as f:
                dictionary_words = [word.replace('غغغ', ' ').rstrip() for word in f.read().splitlines()]
            break
        except UnicodeDecodeError:
            continue

    if not dictionary_words:
        print(f"Failed to open dictionary file with encodings: {encodings}")
        return

    file_words = []
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                file_words = f.read().split()[:100]
            break
        except UnicodeDecodeError:
            continue

    if not file_words:
        print(f"Failed to open file with encodings: {encodings}")
        return

    count = 0
    word_list=[]
    for word in file_words[:100]:
        if word in dictionary_words or word in words.words():
            count += 1
            word_list.append(word)
        if count >= 10:
            return True,count,word_list

    return False

# Usage
file_path = 'english-text.txt'  # replace with your file path
dictionary_path = 'persian_words.txt'  # replace with your dictionary file path
print(detect_meaning(file_path, dictionary_path))
