# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, accuracy_score, roc_curve, auc
from tqdm import tqdm

# Load dataset
csv = "./PhiUSIIL_Phishing_URL_Dataset.csv"
data = pd.read_csv(csv)

# Check basic information
print(data.head())
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Distribution of target variable (assuming 'label' is the target column)
sns.countplot(x='label', data=data)
plt.title('Distribution of Target Variable')
plt.show()

# Drop non-numeric columns that can't be directly used in correlation or models
non_numeric_columns = ['FILENAME', 'URL', 'Domain', 'Title']
data_numeric = data.drop(non_numeric_columns, axis=1)

# Encoding categorical columns (like TLD, if necessary)
label_encoder = LabelEncoder()
data_numeric['TLD_encoded'] = label_encoder.fit_transform(data['TLD'])

# Drop the original 'TLD' column after encoding
data_numeric = data_numeric.drop('TLD', axis=1)

# Descriptive statistics for numeric features
print(data_numeric.describe())

# Visualizations: Histogram and Boxplot with tqdm progress bar
# for col in tqdm(data_numeric.columns[:-1], desc="Plotting Features"):
#     plt.figure(figsize=(10, 4))
    
#     # Histogram
#     plt.subplot(1, 2, 1)
#     sns.histplot(data_numeric[col], kde=True)
#     plt.title(f'Histogram of {col}')
    
#     # Boxplot
#     plt.subplot(1, 2, 2)
#     sns.boxplot(y=data_numeric[col])
#     plt.title(f'Boxplot of {col}')
    
#     plt.show()

# Correlation matrix for numeric features
numeric_columns = data_numeric.select_dtypes(include=[np.number])
corr_matrix = numeric_columns.corr()

# Plot the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=False, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Split dataset into features (X) and target (y)
X = data_numeric.iloc[:, :-1]  # Features (all columns except target 'label')
y = data['label']   # Target

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# SVM model with GridSearch for hyperparameter tuning
svm_model = SVC(probability=True)
param_grid = {
    'kernel': ['linear', 'rbf'], 
    'C': [0.1, 1, 10], 
    'gamma': ['scale', 'auto']
}
svm_grid_search = GridSearchCV(svm_model, param_grid, cv=5, scoring='accuracy')
svm_grid_search.fit(X_train_scaled, y_train)

# Best parameters
print(f"Best parameters for SVM: {svm_grid_search.best_params_}")

# Prediction and evaluation
svm_best_model = svm_grid_search.best_estimator_
y_pred_svm = svm_best_model.predict(X_test_scaled)

# Classification report and Confusion Matrix
print("SVM Classification Report:")
print(classification_report(y_test, y_pred_svm))

print("SVM Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_svm))

# ROC and AUC for SVM
y_pred_svm_prob = svm_best_model.predict_proba(X_test_scaled)[:, 1]
fpr_svm, tpr_svm, _ = roc_curve(y_test, y_pred_svm_prob)
roc_auc_svm = auc(fpr_svm, tpr_svm)

plt.plot(fpr_svm, tpr_svm, label=f'SVM ROC Curve (AUC = {roc_auc_svm:.2f})')
plt.plot([0, 1], [0, 1], linestyle='--')
plt.title('SVM ROC Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()

# KNN model with GridSearch for hyperparameter tuning
knn_model = KNeighborsClassifier()
param_grid_knn = {
    'n_neighbors': [3, 5, 7, 9], 
    'weights': ['uniform', 'distance']
}
knn_grid_search = GridSearchCV(knn_model, param_grid_knn, cv=5, scoring='accuracy')
knn_grid_search.fit(X_train_scaled, y_train)

# Best parameters
print(f"Best parameters for KNN: {knn_grid_search.best_params_}")

# Prediction and evaluation
knn_best_model = knn_grid_search.best_estimator_
y_pred_knn = knn_best_model.predict(X_test_scaled)

# Classification report and Confusion Matrix
print("KNN Classification Report:")
print(classification_report(y_test, y_pred_knn))

print("KNN Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_knn))

# ROC and AUC for KNN
y_pred_knn_prob = knn_best_model.predict_proba(X_test_scaled)[:, 1]
fpr_knn, tpr_knn, _ = roc_curve(y_test, y_pred_knn_prob)
roc_auc_knn = auc(fpr_knn, tpr_knn)

plt.plot(fpr_knn, tpr_knn, label=f'KNN ROC Curve (AUC = {roc_auc_knn:.2f})')
plt.plot([0, 1], [0, 1], linestyle='--')
plt.title('KNN ROC Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()

# Compare SVM and KNN Accuracy
svm_accuracy = accuracy_score(y_test, y_pred_svm)
knn_accuracy = accuracy_score(y_test, y_pred_knn)

print(f"SVM Accuracy: {svm_accuracy:.2f}")
print(f"KNN Accuracy: {knn_accuracy:.2f}")

# Plot ROC for both models
plt.plot(fpr_svm, tpr_svm, label=f'SVM ROC Curve (AUC = {roc_auc_svm:.2f})')
plt.plot(fpr_knn, tpr_knn, label=f'KNN ROC Curve (AUC = {roc_auc_knn:.2f})')
plt.plot([0, 1], [0, 1], linestyle='--')
plt.title('Comparison of ROC Curves')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()
