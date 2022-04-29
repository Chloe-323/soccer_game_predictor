import get_y
import get_x
import importing
import filter_data
import pca
import preprocess
import json
import numpy as np
import logistic

imprt = 0

def main():
    dfs=importing.get_all_tables('data/database.sqlite')
    dfs=filter_data.filter_data(dfs)

    X = [] 
    y = get_y.get_y(dfs)
    if imprt == 1:
        X = get_x.get_x(dfs)
    else: #already imported in training.json
        with open('stuff.json') as f:
            for l in f:
                X.append(json.loads(l))
    # print("X:",len(X))
    #remove skipped rows
    with open('skipped.txt') as f:
        skipped = [int(i) for i in f.read().split(',')]
        y = [y[i] for i in range(len(y)) if i not in skipped]


    # unsupervised learning
    X= np.array(X)

    X=preprocess.normalize(X)

    # X.shape=(21246, 472); reduced about 250 features and maintain 95% variance
    X = pca.pca(X)
    X_train, X_test, y_train, y_test=preprocess.split(X,y)

    # do logistic, svm, and neural network; try different feature transformation
    # and different regularization techniques, and graph them; table of results
    logistic.logistic(X_train, y_train)

if __name__==main():
    main()
