from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.metrics import precision_recall_fscore_support
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def neural_network(X, y, X_test, y_test, hidden_layers):
    classifier = MLPClassifier(hidden_layer_sizes=hidden_layers, activation='tanh', max_iter=4000)
    #number of weights to train
    print("Fitting...")
    classifier.fit(X, y)
    #accuracy
    print("Accuracy: ", classifier.score(X_test, y_test))
    print("F-score: ", precision_recall_fscore_support(y_test, classifier.predict(X_test), average='macro'))
    w_values = classifier.coefs_
    print("Number of weights: ", sum([sum([len(j) for j in i]) for i in w_values]))
    return w_values
