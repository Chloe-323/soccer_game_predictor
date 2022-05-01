import get_y
import get_x
import importing
import filter_data
import pca
import preprocess
import json
import numpy as np
import logistic
import svm
import nn
import sklearn
import sys

imprt = 0

def main():
    print("Importing data...")
    dfs=importing.get_all_tables('data/database.sqlite')
    print("Done importing data.")
    print("Filtering data...")
    dfs=filter_data.filter_data(dfs)
    print("Done filtering data.")

    X = [] 
    y = get_y.get_y(dfs)
    y_one_hot=get_y.get_y_one_hot(dfs)

    print("Getting X...")
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
    print("Done getting X.")

    print("Getting Y...")
    y=np.array(y)
    y_one_hot=np.array(y_one_hot)
    print("Done getting Y.")

    print("Preprocessing data...")
    # unsupervised learning
    X= np.array(X)

    X_normalized=preprocess.normalize(X)
    X_minmax=preprocess.min_max(X)

    # X_minmax.shape=(21246,399)
    # X_normalized.shape=(21246, 472)
    # min_max gets a better result in PCA
    X_minmax = pca.pca(X_minmax)
    X_normalized=pca.pca(X_normalized)
    print("Done preprocessing data.")


    # moved splitting into individual functions for models

    # do logistic, svm, and neural network; try different feature transformation
    # and different regularization techniques, and graph them; table of results
    # logistic.logistic(X_normalized,y)
    # logistic.logistic(X_minmax, y)

    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X_normalized, y_one_hot, test_size=0.2)
    #shape of X_train:
    print("X_train:",X_train.shape)
    #shape of X_test:
    print("X_test:",X_test.shape)
    #shape of y_train:
    print("y_train:",y_train.shape)
    #shape of y_test:
    print("y_test:",y_test.shape)

    if 'logistic' in sys.argv:
        logistic.logistic(X_normalized,y)
    if 'svm' in sys.argv:
        svm.svm(X_normalized,y)
    if 'nn' in sys.argv:
        nn.neural_network(X_train, y_train, X_test, y_test)

    if 'nn' not in sys.argv and 'svm' not in sys.argv and 'logistic' not in sys.argv:
        print("Please specify one or more models to run.")
        print("Usage: python3 main.py [logistic|svm|nn]")



if __name__==main():
    main()
