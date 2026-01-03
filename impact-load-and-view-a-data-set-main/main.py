import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Set Kaggle environment variable (if JSON is in project folder)
# -----------------------------
os.environ['KAGGLE_CONFIG_DIR'] = os.getcwd()  # Current working directory

# -----------------------------
# Download dataset from Kaggle
# -----------------------------
dataset_path = "uciml/autompg-dataset"  # Kaggle dataset identifier
csv_file = "auto-mpg.csv"

# Download dataset (unzip=True extracts the files)
os.system(f"kaggle datasets download -d {dataset_path} --force --unzip")

# -----------------------------
# Load CSV
# -----------------------------
df = pd.read_csv(csv_file)
print("Dataset loaded successfully!\n")

# -----------------------------
# Basic exploration
# -----------------------------
print("First 5 rows of the dataset:")
print(df.head())

print("\nLast 5 rows of the dataset:")
print(df.tail())

print("\nColumns:", df.columns.tolist())
print("\nShape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# -----------------------------
# Fill missing numeric values
# -----------------------------
numeric_cols = df.select_dtypes(include='number').columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# -----------------------------
# Encode categorical columns
# -----------------------------
if 'car_name' in df.columns:
    le = LabelEncoder()
    df['car_name'] = le.fit_transform(df['car_name'])
    print("\nEncoded 'car_name' column:")
    print(df[['car_name']].head())

# -----------------------------
# Drop duplicates
# -----------------------------
df = df.drop_duplicates()
print("\nShape after dropping duplicates:", df.shape)

# -----------------------------
# Final cleaned DataFrame
# -----------------------------
print("\nCleaned DataFrame:")
print(df.head())
