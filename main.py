from data_processing import parse_xml, extract_data, preprocess_data
from vectorization import vectorize_data
from model import train_classifier, evaluate_model

def main():
    # Parse XML data
    train_root = parse_xml('assin-ptbr-train.xml')
    test_root = parse_xml('assin-ptbr-test.xml')

    # Extract data
    train_data, train_labels = extract_data(train_root)
    test_data, test_labels = extract_data(test_root)

    # Preprocess data
    train_data_preprocessed = preprocess_data(train_data)
    test_data_preprocessed = preprocess_data(test_data)

    # Vectorize data
    train_vectorized, test_vectorized, vectorizer = vectorize_data(train_data_preprocessed, test_data_preprocessed)

    # Train classifier
    cls = train_classifier(train_vectorized, train_labels)

    # Evaluate model
    accuracy, report = evaluate_model(cls, test_vectorized, test_labels)

    print("Accuracy:", accuracy)
    print("Classification Report:\n", report)

if __name__ == "__main__":
    main()
