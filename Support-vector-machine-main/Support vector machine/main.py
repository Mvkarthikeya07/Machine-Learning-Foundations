import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn import metrics

# Load dataset
data = pd.read_csv("spam (2).csv", encoding='Windows-1252')

# Display last 5 rows
print("Last 5 rows:\n", data.tail())

# Check for missing values
print("\nMissing values:\n", data.isnull().sum())

# Assign features and labels
X = data['v2'].values  # Text messages
y = data['v1'].values  # Labels (spam/ham)
print("\nFeature shape:", X.shape)
print("Label shape:", y.shape)

# Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)
print("\nTraining set size:", X_train.shape[0])
print("Test set size:", X_test.shape[0])

# Convert text data into numerical features
cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
X_test = cv.transform(X_test)
print("\nX_train shape after CountVectorizer:", X_train.shape)
print("X_test shape after CountVectorizer:", X_test.shape)

# Train the SVM classifier
svc = SVC()
svc.fit(X_train, y_train)

# Make predictions on the test set
y_pred = svc.predict(X_test)
print("\nPredictions:\n", y_pred)

# Evaluate the model
accuracy = metrics.accuracy_score(y_test, y_pred)
print("\nAccuracy of the model:", accuracy)
print("\nClassification Report:\n", metrics.classification_report(y_test, y_pred))
print("Confusion Matrix:\n", metrics.confusion_matrix(y_test, y_pred))
