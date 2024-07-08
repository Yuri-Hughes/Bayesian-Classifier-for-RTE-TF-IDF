from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import nltk

nltk.download("stopwords")

def vectorize_data(train_data, test_data):
    vectorizer = TfidfVectorizer(stop_words=nltk.corpus.stopwords.words('portuguese'), max_features=1000, decode_error="ignore")
    vectorizer.fit(train_data)
    train_vectorized = vectorizer.transform(train_data)
    test_vectorized = vectorizer.transform(test_data)
    return train_vectorized, test_vectorized, vectorizer
