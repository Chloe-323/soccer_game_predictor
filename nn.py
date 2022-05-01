from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def neural_network(X, y, X_test, y_test):
    print("Neural Network")
    classifier = MLPClassifier(hidden_layer_sizes=(32, 32, 32, 32, 32), max_iter=1000)
    #number of parameters
    print("Fitting...")
    classifier.fit(X, y)
    # get R^2 value
    print("Training R^2:", classifier.score(X, y))
    #test
    print("Test R^2:", classifier.score(X_test, y_test))
    w_values = classifier.coefs_
    return w_values
