import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load the dataset (make sure the file is in the same folder as this script)
dataset = pd.read_csv("student_scores .csv")  # Note the space before .csv
print("First 5 rows:\n", dataset.head())
print("\nLast 5 rows:\n", dataset.tail())
print("\nDataset Info:")
dataset.info()

# Assigning Hours to X and Scores to Y
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

print("\nFeatures (X):\n", X)
print("\nTarget (Y):\n", Y)

# Split dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1/3, random_state=0)

# Train the Linear Regression model
reg = LinearRegression()
reg.fit(X_train, Y_train)

# Make predictions
Y_pred = reg.predict(X_test)
print("\nPredicted Values:\n", Y_pred)
print("\nActual Values:\n", Y_test)

# Calculate error metrics
mse = mean_squared_error(Y_test, Y_pred)
mae = mean_absolute_error(Y_test, Y_pred)
rmse = np.sqrt(mse)

print("\nError Metrics:")
print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)

# Optional: Plot the regression line
plt.scatter(X, Y, color='blue', label='Actual Scores')
plt.plot(X, reg.predict(X), color='red', label='Regression Line')
plt.title('Hours Studied vs Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.legend()
plt.show()
