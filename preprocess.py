from sklearn import preprocessing
from sklearn.model_selection import train_test_split

def preprocess(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    scaler = preprocessing.StandardScaler().fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test