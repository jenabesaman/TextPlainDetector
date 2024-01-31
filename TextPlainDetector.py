import nltk
import joblib
import numpy as np

class TextPlainDetector:
    def __init__(self, InString: str):
        self.text = [InString]

    def predicting(self):
        vectorizer, model = joblib.load('model_and_vectorizer.pkl')
        tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
        texts = [tokenizer.tokenize(text.lower())[:20] for text in self.text]
        texts = [word for text in texts for word in text]
        features = vectorizer.transform(texts)
        predictions = model.predict(features)
        percentage_similar = np.mean(predictions) * 100
        # similar_words = [word for word, pred in zip(texts, predictions) if pred]
        if percentage_similar >= 96:
            return True
        else:
            return False