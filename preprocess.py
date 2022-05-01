from sklearn import preprocessing
from sklearn.model_selection import train_test_split


def normalize(X):
    scaler = preprocessing.StandardScaler().fit(X)
    X=scaler.transform(X)
    return X