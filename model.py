from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

def train_classifier(train_vectorized, train_labels):
    cls = MultinomialNB()
    cls.fit(train_vectorized, train_labels)
    return cls

def evaluate_model(cls, test_vectorized, test_labels):
    y_pred = cls.predict(test_vectorized)
    accuracy = accuracy_score(test_labels, y_pred)
    report = classification_report(test_labels, y_pred)
    return accuracy, report
