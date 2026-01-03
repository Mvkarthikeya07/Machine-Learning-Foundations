from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree 
import matplotlib.pyplot as plt 
# Load the Iris dataset 
data = load_iris() 
X, y = data.data, data.target 
# Split the dataset into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 
# Create a Decision Tree classifier 
clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42) 
# Train the classifier 
clf.fit(X_train, y_train) 
# Make predictions on the test set 
y_pred = clf.predict(X_test) 
# Evaluate the model 
accuracy = clf.score(X_test, y_test) 
print(f'Accuracy: {accuracy:.2f}') 
# Visualize the Decision Tree 
plt.figure(figsize=(12, 8)) 
tree.plot_tree(clf, feature_names=data.feature_names, class_names=data.target_names, filled=True) 
plt.show()
