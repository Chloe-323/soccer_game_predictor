from sklearn import preprocessing
from sklearn.model_selection import train_test_split

def split(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    return X_train, X_test, y_train, y_test

def normalize(X):
    scaler = preprocessing.StandardScaler().fit(X)
    X=scaler.transform(X)
    return X