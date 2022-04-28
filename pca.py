from sklearn.decomposition import PCA

def pca(X):
    # eliminate half of the features
    pca=PCA(n_components=X.shape[1]/2)
    X=pca.fit(X)
    print(f"The variance maintained is {pca.explained_variance_ratio_}")
    return X
