import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Generate synthetic data
# -----------------------------
def generate_data(num_samples=300, n_centers=4, random_seed=42):
    np.random.seed(random_seed)
    points_per_center = num_samples // n_centers
    centers = np.random.uniform(-10, 10, (n_centers, 2))
    X = np.vstack([center + np.random.randn(points_per_center, 2) for center in centers])
    return X

# -----------------------------
# Euclidean distance
# -----------------------------
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# -----------------------------
# Compute distance matrix
# -----------------------------
def compute_distance_matrix(X):
    num_samples = X.shape[0]
    distance_matrix = np.zeros((num_samples, num_samples))
    for i in range(num_samples):
        for j in range(i + 1, num_samples):
            d = euclidean_distance(X[i], X[j])
            distance_matrix[i, j] = d
            distance_matrix[j, i] = d
    return distance_matrix

# -----------------------------
# Agglomerative Clustering
# -----------------------------
def hierarchical_clustering(X, n_clusters=4):
    num_samples = X.shape[0]
    distances = compute_distance_matrix(X)
    
    clusters = [[i] for i in range(num_samples)]
    
    while len(clusters) > n_clusters:
        min_dist = float('inf')
        to_merge = (None, None)
        
        # Find the closest pair of clusters
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                d = np.min([distances[p][q] for p in clusters[i] for q in clusters[j]])
                if d < min_dist:
                    min_dist = d
                    to_merge = (i, j)
        
        # Merge clusters
        i, j = to_merge
        clusters[i].extend(clusters[j])
        del clusters[j]
    
    return clusters

# -----------------------------
# Extract cluster labels
# -----------------------------
def extract_cluster_labels(clusters, n_samples):
    labels = np.zeros(n_samples, dtype=int)
    for cluster_id, cluster in enumerate(clusters):
        for idx in cluster:
            labels[idx] = cluster_id
    return labels

# -----------------------------
# Example usage
# -----------------------------
X = generate_data(num_samples=300, n_centers=4)
clusters = hierarchical_clustering(X, n_clusters=4)
labels = extract_cluster_labels(clusters, X.shape[0])

# Plot clusters
plt.figure(figsize=(8,6))
for cluster_id in np.unique(labels):
    plt.scatter(X[labels == cluster_id, 0], X[labels == cluster_id, 1], label=f'Cluster {cluster_id}')
plt.title("Hierarchical Clustering")
plt.xlabel("X1")
plt.ylabel("X2")
plt.legend()
plt.show()
