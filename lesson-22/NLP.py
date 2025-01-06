import pandas as pd
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from nltk import NaiveBayesClassifier, classify
import nltk

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load dataset (replace with your file path)
data = pd.read_csv('SMSSpamCollection.csv', sep='\t', header=None, names=['Label', 'Message'])

# Encode labels ('ham' -> 0, 'spam' -> 1)
data['Label'] = data['Label'].map({'ham': 0, 'spam': 1})

print(data.head())

# Preprocessing function
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Apply preprocessing to messages
data['Processed_Message'] = data['Message'].apply(preprocess_text)

# Create feature extraction function
def extract_features(message):
    return {word: True for word in message}

# Prepare data for training
features = [(extract_features(msg), label) for msg, label in zip(data['Processed_Message'], data['Label'])]

# Split into training and testing sets
train_data, test_data = train_test_split(features, test_size=0.2, random_state=42)

# Train Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_data)

# Evaluate the model
accuracy = classify.accuracy(classifier, test_data)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Show most informative features
classifier.show_most_informative_features(10)

# Example classification
def classify_message(message):
    tokens = preprocess_text(message)
    features = extract_features(tokens)
    return 'spam' if classifier.classify(features) == 1 else 'ham'

# Test example
example_message = "Congratulations! You have won a $1000 Walmart gift card. Click here to claim."
print(f"Message: {example_message}\nClassified as: {classify_message(example_message)}")
