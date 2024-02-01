import nltk
import joblib
import numpy as np
# from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
# vectorizer = CountVectorizer()
# Load the model from the pickle file
# Load the vectorizer and the model


# vectorizer, model = joblib.load('model_and_vectorizer.pkl')

# Assume we have a list of file paths
# file_paths = ["farsi-text.txt"]  # list of file paths

# def read_file_as_text(file_path, encodings):
#     for encoding in encodings:
#         try:
#             with open(file_path, 'r', encoding=encoding) as file:
#                 return file.read()
#         except UnicodeDecodeError:
#             pass
#     # If the provided encodings fail, try 'latin-1'
#     try:
#         with open(file_path, 'rb') as file:
#             return file.read().decode('latin-1')
#     except UnicodeDecodeError:
#         print(f'Could not read {file_path} with any of the provided encodings.')
#         return ''

import base64
import io


class TextPlainDetector:
    def __init__(self, InString: str):
        # self.base64_string = base64_string
        self.text = [InString]

    def predicting(self):
        # self.text=self.read_base64_as_text()
        vectorizer, model = joblib.load('model_and_vectorizer.pkl')
        tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
        texts = [tokenizer.tokenize(text.lower())[:20] for text in self.text]
        texts = [word for text in texts for word in text]
        features = vectorizer.transform(texts)
        predictions = model.predict(features)
        percentage_similar = np.mean(predictions) * 100
        similar_words = [word for word, pred in zip(texts, predictions) if pred]
        if percentage_similar >= 96:
            return True
        else:
            return False


# raw_text = text = r"""" با سلام و احترام
# بدینوسیله به استحضار آن مقام محترم می رساند نظر به  افزایش روزافزون نرخ تورم و تحمیل آن به پیکر قشر حقوق بگیر، تناسب دخل و خرج خانواده را به نحوی بر هم ریخته که به‌هیچ‌عنوان دریافتی جاری حداقل نیازهای اولیه را نیز تأمین نمی‌نماید، لذا خواهشمند است با توجه به این که این‌جانب منبع درآمد دیگری غیر از این شرکت برای تأمین معاش خود ندارم، عنایت فرموده دستور تجدید نظر در حقوق دریافتی بنده را امر به ابلاغ فرمایید.
# """
#
# obj = TextPlainDetector(InString=raw_text)
# print(obj.predicting())




# text=raw_text.encode('unicode_escape').decode()

# #texts = [read_file_as_text(file_path, ['utf-8', 'windows-1256', 'latin-1']) for file_path in file_paths]
#
# # Read the texts from the files
#
# # Tokenize the text and convert to lower case
# tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
# texts = [tokenizer.tokenize(text.lower())[:50] for text in texts]  # Only take the first 20 words
#
# # Flatten the texts
# texts = [word for text in texts for word in text]
#
# # Convert the texts to features using the same vectorizer
# features = vectorizer.transform(texts)
#
# # Make predictions on the texts
# predictions = model.predict(features)
# print(predictions)
# # Calculate the percentage of words that are similar to dictionary words
# percentage_similar = np.mean(predictions) * 100
# print(percentage_similar)
# # Print out whether the text is similar to the dictionary words
# if percentage_similar >= 95:
#     print('The text is similar to the dictionary words.')
# else:
#     print('The text is not similar to the dictionary words.')
#
#
# # Get words that are predicted as similar to dictionary words
# similar_words = [word for word, pred in zip(texts, predictions) if pred]
#
# print('Words similar to dictionary words:', similar_words)
