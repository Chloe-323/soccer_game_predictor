from sklearn.decomposition import PCA

def pca(X):
    # eliminate half of the features
    pca=PCA(n_components=.95)
    pca.fit(X)
    X= pca.transform(X)
    return X
