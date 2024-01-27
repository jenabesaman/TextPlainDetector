import pickle
#
# import nltk
# from nltk.corpus import words
#
# nltk.download('words')
#
# english_words=set(words.words())
#
# def check_words(file_path):
#     with open(file_path,'rb') as file:
#         data=file.read()
#
#         text=data.decode('utf-8',errors='ignore')
#         word_list=text.split()[:20]
#         meaningful_words=[word for word in word_list if word.lower()
#                           in english_words]
#         return len(meaningful_words) >=5
# print(check_words("C:/Workarea/MimetypeDocksDetect/DocksEnglish.py"))


# import os
# from hazm import Lemmatizer, word_tokenize
#
# def check_words(file_path):
#     lemmatizer = Lemmatizer()
#     with open(file_path, 'rb') as file:
#         data = file.read().decode(errors='replace')
#     words = word_tokenize(data)
#     meaningful_count = 0
#     for word in words[:20]:
#         print(lemmatizer.lemmatize(word))
#         if lemmatizer.lemmatize(word) != word:
#             meaningful_count += 1
#     return meaningful_count >= 1
#
# print(check_words(file_path=r"C:/Workarea/MimetypeDocksDetect/farsi.txt"))

import nltk
from nltk.corpus import words
from hazm import Lemmatizer, word_tokenize

nltk.download('words')

english_words = set(words.words())
lemmatizer = Lemmatizer()

def check_words(file_path):
    with open(file_path, 'rb') as file:
        data = file.read().decode(errors='replace')
    words = word_tokenize(data)
    meaningful_count = 0
    for word in words[:200]:
        if word.lower() in english_words or lemmatizer.lemmatize(word) != word:
            meaningful_count += 1
    return meaningful_count >= 10

print(check_words(r"C:/Workarea/MimetypeDocksDetect/farsi.txt"))


# print(check_words(file_path=r"C:/Workarea/MimetypeDocksDetect/farsi.txt"))