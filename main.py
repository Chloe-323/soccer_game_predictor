import get_y
import get_x
import importing
import filter_data
import pca
import preprocess
import json
import numpy as np

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



    # normalizing stuff, split into test and train sets
    X_train, X_test, y_train, y_test=preprocess.preprocess(X,y)

    # unsupervised learning
    X= np.array(X)
    X = pca.pca(X)

    # do logistic, svm, and neural network; try different feature transformation
    # and different regularization techniques, and graph them; table of results




if __name__==main():
    main()
