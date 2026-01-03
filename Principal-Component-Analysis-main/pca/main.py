# -----------------------------
# Imports
# -----------------------------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# -----------------------------
# 1. Load dataset
# -----------------------------
wine = load_wine()
X = wine.data
y = wine.target

# -----------------------------
# Standardize features (important for PCA)
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# 2. Train/test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42, stratify=y
)

# -----------------------------
# 3. Logistic Regression WITHOUT PCA
# -----------------------------
clf_no_pca = LogisticRegression(max_iter=500)
clf_no_pca.fit(X_train, y_train)
y_pred_no_pca = clf_no_pca.predict(X_test)
acc_no_pca = accuracy_score(y_test, y_pred_no_pca)
print("Accuracy without PCA:", acc_no_pca)

# -----------------------------
# 4. Logistic Regression WITH PCA (reduce to 2 components)
# -----------------------------
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

clf_pca = LogisticRegression(max_iter=500)
clf_pca.fit(X_train_pca, y_train)
y_pred_pca = clf_pca.predict(X_test_pca)
acc_pca = accuracy_score(y_test, y_pred_pca)
print("Accuracy with PCA (2 components):", acc_pca)

# -----------------------------
# Optional: plot the 2D PCA projection
# -----------------------------
plt.figure(figsize=(8,6))
for target in np.unique(y):
    plt.scatter(
        X_train_pca[y_train == target, 0],
        X_train_pca[y_train == target, 1],
        label=wine.target_names[target]
    )
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("Wine dataset PCA projection")
plt.legend()
plt.show()
