from sklearn import preprocessing


def normalize(X):
    scaler = preprocessing.StandardScaler().fit(X)
    X=scaler.transform(X)
    return X

def min_max(X,min=0,max=1):
    scaler=preprocessing.MinMaxScaler(feature_range=(min,max))
    X=scaler.fit_transform(X)
    return X
