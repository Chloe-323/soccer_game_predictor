from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_fscore_support

# i love copy and pasting
def logistic(X_train,y_train):

    # does not regularize and transform
    logreg = LogisticRegression(C=100000000)
    logreg.fit(X_train, y_train)
    y_hat_logreg = logreg.predict(X_train)
    acc_logreg = logreg.score(X_train, y_train)
    print("Accuracy on training data = %f" % acc_logreg)
    w_logreg = logreg.coef_
    intercept_logreg = logreg.intercept_
    print('w_logreg: ', w_logreg)
    print('intercept_logreg: ', intercept_logreg)
    prec, recal, fscore,support=precision_recall_fscore_support(y_train,y_hat_logreg)
    print('precision: ', prec)
    print('recall: ', recal)
    print('fscore: ', fscore)

    # add feature transformation and regularization here