# main.py

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('data.csv')

# Display first few rows
print("First 5 rows of dataset:")
print(data.head())

# Drop unnecessary columns (specific to Kaggle dataset)
if 'Id' in data.columns:
    data.drop(['Id'], axis=1, inplace=True)

# Handle missing values (simple method: drop rows with missing data)
data = data.dropna(subset=['GrLivArea', 'TotalBsmtSF', 'OverallQual', 'GarageCars', 'SalePrice'])

# Select features and target
X = data[['GrLivArea', 'TotalBsmtSF', 'OverallQual', 'GarageCars']]  # Input features
y = data['SalePrice']  # Target column

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("\nModel Performance:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Plot predictions vs actual
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()
