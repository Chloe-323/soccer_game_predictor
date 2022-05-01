from sklearn import preprocessing


def normalize(X):
    scaler = preprocessing.StandardScaler().fit(X)
    X=scaler.transform(X)
    return X

def min_max(X,min=0,max=1):
    scaler=preprocessing.MinMaxScaler(feature_range=(min,max))
    X=scaler.fit_transform(X)
    return X

def train_test_split(X, y):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test
