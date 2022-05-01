from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_fscore_support
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.kernel_approximation import Nystroem


def logistic(X,y):
    #stratification did not change anything
    X_train, X_test, y_train, y_test=train_test_split(X, y,stratify=y,
                                                      test_size=0.25)

    y_train = LabelEncoder().fit_transform(y_train)
    y_test = LabelEncoder().fit_transform(y_test)
    # L2 regularization; one-versus-rest
    choose_regularization(X_test, X_train, y_test, y_train,100000000)
    # training fscore:  [0.67586285 0.16028997 0.53306052]; accuracy .553910
    # testing fscore:  [0.6493913  0.11163895 0.49467085]; accuracy .517696
    choose_regularization(X_test, X_train, y_test, y_train,.01)
    choose_regularization(X_test, X_train, y_test, y_train,.0001)
    # conclusion: no significant impact on accuracy. More regularization
    # sacrifices performance of draw to home win and away win, but does
    # increase test accuracy and decrease training accuracy

    # L1 regularization; one-versus-rest
    choose_regularization(X_test, X_train, y_test, y_train,100000000,'l1')
    choose_regularization(X_test, X_train, y_test, y_train,.01,'l1')
    choose_regularization(X_test, X_train, y_test, y_train,.0001,'l1')
    # conclusion: f-score for draw become 0 as C become smaller, therefore
    # making the overall accuracy decrease

    # Multinomial multi_class
    multinomial(X_test,X_train,y_test,y_train)
    # noticeable increase of fscore in draw scenarios

    # dual_formalization(X_test,X_train,y_test,y_train)
    # general decrease of performance; commented because it's slow

    # polynomial transformation via Nystroem kernel approximation: try 2 to 5
    # degrees pure polynomial transformation is too slow: 3min in but still
    # cannot output degree 2
    polynomial_transformation(X_test,X_train,y_test,y_train)
    # conclusion: no significant changes on training error, though test error
    # increases significantly, especially on away win and draw scenarios.
    # This is presumably due to overfitting

def polynomial_transformation(X_test, X_train, y_test, y_train):
    for i in range(2,6):
        print(f"Polynomial: degree {i}")
        feature_map_nystroem = Nystroem(degree=i)
        X_transformed=feature_map_nystroem.fit_transform(X_train)
        X_test_transformed=feature_map_nystroem.fit_transform(X_test)
        logreg = LogisticRegression(solver='saga') # lbfgs cannot converge, saga can
        train_and_print_info(X_test_transformed, X_transformed, logreg, y_test, y_train)

def choose_regularization(X_test, X_train, y_test, y_train,C=100000000.,penalty_term='l2'):
    print(f"C={C}")
    logreg = LogisticRegression(C=C, multi_class='ovr',penalty=penalty_term,solver='liblinear' if penalty_term=='l1' else 'lbfgs')
    train_and_print_info(X_test, X_train, logreg, y_test, y_train)


def multinomial(X_test, X_train, y_test, y_train):
    # does not regularize and transform
    print("Multinomial with no regularization")
    logreg = LogisticRegression(C=100000000, multi_class='multinomial')
    train_and_print_info(X_test, X_train, logreg, y_test, y_train)


def dual_formalization(X_test, X_train, y_test, y_train):
    # does not regularize and transform
    print("Dual formalization with no regularization")
    logreg = LogisticRegression(C=100000000, multi_class='ovr', dual=True,
                                solver='liblinear')
    train_and_print_info(X_test, X_train, logreg, y_test, y_train)


def train_and_print_info(X_test, X_train, logreg, y_test, y_train):
    logreg.fit(X_train, y_train)
    y_hat_logreg = logreg.predict(X_train)
    w_logreg = logreg.coef_
    intercept_logreg = logreg.intercept_
    print('w_logreg: ', w_logreg)
    print('intercept_logreg: ', intercept_logreg)
    acc_logreg = logreg.score(X_train, y_train)
    print("Accuracy on training data = %f" % acc_logreg)
    prec, recal, fscore, support = precision_recall_fscore_support(y_train,
                                                                   y_hat_logreg)
    print('precision: ', prec)
    print('recall: ', recal)
    print('fscore: ', fscore)
    print()
    # test data
    print("Test data")
    y_hat_logreg = logreg.predict(X_test)
    acc_logreg = logreg.score(X_test, y_test)
    print("Accuracy on test data = %f" % acc_logreg)
    prec, recal, fscore, support = precision_recall_fscore_support(y_test,
                                                                   y_hat_logreg)
    print('precision: ', prec)
    print('recall: ', recal)
    print('fscore: ', fscore)
    print()

