from sklearn.cluster import KMeans

def predict_clusters(X_word2vec):
    num_clusters = 10
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X_word2vec)
    return kmeans.labels_

