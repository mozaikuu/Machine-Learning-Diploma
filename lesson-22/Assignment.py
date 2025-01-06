# Assignment: Text Classification Using IMDb Review Dataset

# ## Step 1: Data Loading
import pandas as pd
from sklearn.model_selection import train_test_split

# Load IMDb Movie Reviews dataset
dataset_path = './IMDB_Dataset.csv'  # 50,000 dataset split evenly
data = pd.read_csv(dataset_path)

# Inspect the dataset
data.head()

# Split dataset into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# ## Step 2: Data Preprocessing
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Text cleaning function
def clean_text(text):
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^a-zA-Z]', ' ', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

# Apply text cleaning
data['cleaned_text'] = data['review'].apply(clean_text)

# ## Step 3: Feature Extraction
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Bag of Words (BoW)
vectorizer_bow = CountVectorizer(max_features=5000)
bow_features = vectorizer_bow.fit_transform(data['cleaned_text'])

# TF-IDF
vectorizer_tfidf = TfidfVectorizer(max_features=5000)
tfidf_features = vectorizer_tfidf.fit_transform(data['cleaned_text'])

# Word Embeddings
from gensim.models import Word2Vec

tokenized_reviews = [word_tokenize(text) for text in data['cleaned_text']]
word2vec_model = Word2Vec(sentences=tokenized_reviews, vector_size=100, window=5, min_count=1)

# Deep Learning Embeddings (BERT)
from transformers import BertTokenizer, BertModel
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert_model = BertModel.from_pretrained('bert-base-uncased')

def extract_bert_features(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
    outputs = bert_model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

bert_features = [extract_bert_features(text) for text in data['cleaned_text']]

# ## Step 4: Model Training
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Naive Bayes
nb_model = MultinomialNB()
bow_train, bow_test = train_test_split(bow_features, test_size=0.2, random_state=42)
nb_model.fit(bow_train, train_data['sentiment'])

# Support Vector Machine
svm_model = SVC(class_weight='balanced', probability=True)
svm_model.fit(bow_train, train_data['sentiment'])

# Logistic Regression
lr_model = LogisticRegression(class_weight='balanced')
lr_model.fit(bow_train, train_data['sentiment'])

# ## Step 5: Model Evaluation
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

# Function to evaluate model
def evaluate_model(model, test_features, test_labels):
    predictions = model.predict(test_features)
    print(classification_report(test_labels, predictions))
    cm = confusion_matrix(test_labels, predictions)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.show()
    print("AUC-ROC:", roc_auc_score(test_labels, model.predict_proba(test_features)[:, 1]))

# Evaluate models
evaluate_model(nb_model, bow_test, test_data['sentiment'])
evaluate_model(svm_model, bow_test, test_data['sentiment'])
evaluate_model(lr_model, bow_test, test_data['sentiment'])

# ## Step 6: Hyperparameter Tuning
from sklearn.model_selection import GridSearchCV

# Example: Hyperparameter tuning for Logistic Regression
param_grid = {'C': [0.1, 1, 10, 100]}
grid_search = GridSearchCV(LogisticRegression(class_weight='balanced'), param_grid, cv=5, scoring='f1')
grid_search.fit(bow_train, train_data['sentiment'])

print("Best Parameters:", grid_search.best_params_)

