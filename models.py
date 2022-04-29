from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def logistic_regression(X_train, y_train, X_test, y_test):
    print("Logistic Regression")
    regressor = LogisticRegression()
    print("Fitting...")
    regressor.fit(X_train, y_train)
    # get R^2 value
    r_sq = regressor.score(X_test, y_test)
    w_values = regressor.coef_
    print("R^2: ", r_sq)
    print("Weights: ", w_values)
    return r_sq

def linear_regression(X_train, y_train, X_test, y_test):
    print("Linear Regression")
    regressor = LinearRegression()
    print("Fitting...")
    regressor.fit(X_train, y_train)
    # get R^2 value
    r_sq = regressor.score(X_test, y_test)
    w_values = regressor.coef_
    print("R^2: ", r_sq)
    print("Weights: ", w_values)
    return r_sq

def SVM(X_train, y_train, X_test, y_test):
    print("SVM")
    regressor = SVR(kernel='rbf')
    print("Fitting...")
    regressor.fit(X_train, y_train)
    # get R^2 value
    r_sq = regressor.score(X_test, y_test)
    print("R^2: ", r_sq)
    print("Weights: ", regressor.coef_)
    return r_sq

def neural_network(X_train, y_train, X_test, y_test):
    print("Neural Network")
    regressor = MLPRegressor(hidden_layer_sizes=(100,100,100), max_iter=1000)
    print("Fitting...")
    regressor.fit(X_train, y_train)
    # get R^2 value
    r_sq = regressor.score(X_test, y_test)
    w_values = regressor.coefs_
    print("R^2: ", r_sq)
    print("Weights: ", w_values)
    return r_sq
