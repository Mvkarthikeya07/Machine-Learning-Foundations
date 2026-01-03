import os
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix, accuracy_score
from scipy.stats import mode
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# -----------------------------
# Silence Loky CPU warning on Windows
# -----------------------------
os.environ["LOKY_MAX_CPU_COUNT"] = str(os.cpu_count())

# -----------------------------
# Load Iris dataset
# -----------------------------
iris = load_iris()
X = iris.data
y = iris.target  # Actual labels

# -----------------------------
# Apply KMeans clustering
# -----------------------------
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)  # n_init avoids warning
y_kmeans = kmeans.fit_predict(X)

# -----------------------------
# Create DataFrame for clarity
# -----------------------------
df = pd.DataFrame(X, columns=iris.feature_names)
df['Actual'] = y
df['Cluster'] = y_kmeans

print("Cluster Centers:\n", kmeans.cluster_centers_)
print("\nSample clustered data:\n", df.head())

# -----------------------------
# Map clusters to actual labels
# -----------------------------
def map_clusters_to_labels(y_true, y_pred):
    labels = np.zeros_like(y_pred)
    for i in range(3):  # Number of clusters
        mask = (y_pred == i)
        if np.any(mask):
            labels[mask] = mode(y_true[mask])[0]
    return labels

y_kmeans_mapped = map_clusters_to_labels(y, y_kmeans)

# -----------------------------
# Confusion matrix and accuracy
# -----------------------------
cm = confusion_matrix(y, y_kmeans_mapped)
acc = accuracy_score(y, y_kmeans_mapped)

print("\nConfusion Matrix:\n", cm)
print("\nClustering Accuracy:", acc)

# -----------------------------
# Optional: PCA 2D visualization
# -----------------------------
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

plt.figure(figsize=(8,6))
for cluster in np.unique(y_kmeans_mapped):
    plt.scatter(
        X_pca[y_kmeans_mapped == cluster, 0],
        X_pca[y_kmeans_mapped == cluster, 1],
        label=f"Cluster {cluster}"
    )

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    color='black', marker='X', s=200, label='Centroids'
)

plt.title("KMeans Clustering on Iris Dataset (PCA-reduced 2D)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend()
plt.show()
