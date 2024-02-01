import nltk
import joblib
import numpy as np

class TextPlainDetector:
    def __init__(self, InString: str,vectorizer,model):
        self.text = [InString]
        self.vectorizer = vectorizer
        self.model = model

    def predicting(self):
        # vectorizer, model = joblib.load('model_and_vectorizer2.pkl')
        tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
        texts = [tokenizer.tokenize(text.lower())[:20] for text in self.text]
        texts = [word for text in texts for word in text]
        features = self.vectorizer.transform(texts)
        predictions = self.model.predict(features)
        percentage_similar = np.mean(predictions) * 100
        # similar_words = [word for word, pred in zip(texts, predictions) if pred]
        if percentage_similar >= 80:
            return True
        else:
            return False
# textPlainDetector=TextPlainDetector("")