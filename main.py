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
    y_one_hot=get_y.get_y_one_hot(dfs)

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
        y_one_hot = [y_one_hot[i] for i in range(len(y_one_hot)) if i not in skipped]
    f.close()

    y=np.array(y)
    y_one_hot=np.array(y_one_hot)

    # unsupervised learning
    X= np.array(X)

    X_normalized=preprocess.normalize(X)
    X_minmax=preprocess.min_max(X)

    # X_minmax.shape=(21246,399)
    # X_normalized.shape=(21246, 472)
    # min_max gets a better result in PCA
    X_minmax = pca.pca(X_minmax)
    X_normalized=pca.pca(X_normalized)


    # moved splitting into individual functions for models

    # do logistic, svm, and neural network; try different feature transformation
    # and different regularization techniques, and graph them; table of results
    # logistic.logistic(X_normalized,y)
    # logistic.logistic(X_minmax, y)




if __name__==main():
    main()
