from sklearn.metrics import precision_recall_fscore_support
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import svm
import numpy as np

# this runs very slowly... please see results from svm_results.txt


def svm_model(X,y):
    X_train, X_test, y_train, y_test=train_test_split(X, y,stratify=y,
                                                      test_size=0.25)
    y_train = LabelEncoder().fit_transform(y_train)
    y_test = LabelEncoder().fit_transform(y_test)
    # L2 regularization; one-versus-rest
    # choose_regularization(X_test, X_train, y_test, y_train)
    #choose_regularization(X_test, X_train, y_test, y_train, .01)
    #choose_regularization(X_test, X_train, y_test, y_train, .0001)

    from joblib import parallel_backend

    with parallel_backend('threading',n_jobs=-1):
        linear_kernel(X_test,X_train,y_test,y_train)

        polynomial_kernel(X_test,X_train,y_test,y_train)

        rbf_kernel(X_test,X_train,y_test,y_train)


def rbf_kernel(X_test,X_train,y_test,y_train):
    for i in range(2,6):
        print(f"RBF Kernel: degree{i}")
        for j in [1,.01,.0001]:
            svm_class = svm.SVC(C=j, degree=i, kernel='rbf')
            non_linear_train_and_print_info(X_test, X_train, svm_class, y_test, y_train)



def polynomial_kernel(X_test, X_train, y_test, y_train):
    for i in range(2,6):
        print(f"Polynomial Kernel: degree{i}")
        for j in [1,.01,.0001]:
            svm_class = svm.SVC(C=j, degree=i, kernel='poly')
            non_linear_train_and_print_info(X_test, X_train, svm_class, y_test, y_train)

def linear_kernel(X_test, X_train, y_test, y_train):
    for i in range(4,6):
        for j in [1,.01,.0001]:
            if i==4 and j==1:
                continue # just did it before stopping and make editions
            print(f"Linear Kernel: degree{i}; C={j}")
            svm_class = svm.SVC(C=j, degree=i, kernel='linear')
            train_and_print_info(X_test, X_train, svm_class, y_test, y_train)


def choose_regularization(X_test, X_train, y_test, y_train,C=1.):
    print(f"C={C}")
    svm_class = svm.SVC(C=C,degree=1,kernel='linear')
    train_and_print_info(X_test, X_train, svm_class, y_test, y_train)

def train_and_print_info(X_test, X_train, svm_class, y_test, y_train):
    svm_class.fit(X_train, y_train)
    y_hat_svm_class = svm_class.predict(X_train)
    w_svm_class = svm_class.coef_
    intercept_svm_class = svm_class.intercept_
    with np.printoptions(threshold=np.inf):
        print('w_svm_class: ', w_svm_class)
        print('/w_svm_class')
        print()
        print('indices for support vectors',svm_class.support_)
        print('/indices for support vectors')
        print()
    print('intercept_svm_class: ', intercept_svm_class)
    print('number of support vectors',svm_class.n_support_)
    acc_svm_class = svm_class.score(X_train, y_train)
    print("Accuracy on training data = %f" % acc_svm_class)
    prec, recal, fscore, support = precision_recall_fscore_support(y_train,
                                                             y_hat_svm_class)
    print('precision: ', prec)
    print('recall: ', recal)
    print('fscore: ', fscore)
    print()
    # test data
    print("Test data")
    y_hat_svm_class = svm_class.predict(X_test)
    acc_svm_class = svm_class.score(X_test, y_test)
    print("Accuracy on test data = %f" % acc_svm_class)
    prec, recal, fscore, support = precision_recall_fscore_support(y_test,
                                                              y_hat_svm_class)
    print('precision: ', prec)
    print('recall: ', recal)
    print('fscore: ', fscore)
    print()

def non_linear_train_and_print_info(X_test, X_train, svm_class, y_test, y_train):
    svm_class.fit(X_train, y_train)
    y_hat_svm_class = svm_class.predict(X_train)
    w_svm_class = svm_class.dual_coef_
    intercept_svm_class = svm_class.intercept_
    with np.printoptions(threshold=np.inf):
        print('w_svm_class(dual): ', w_svm_class)
        print('indices for support vectors',svm_class.support_)
    print('intercept_svm_class: ', intercept_svm_class)
    print('number of support vectors',svm_class.n_support_)
    acc_svm_class = svm_class.score(X_train, y_train)
    print("Accuracy on training data = %f" % acc_svm_class)
    prec, recal, fscore, support = precision_recall_fscore_support(y_train,
                                                             y_hat_svm_class)
    print('precision: ', prec)
    print('recall: ', recal)
    print('fscore: ', fscore)
    print()
    # test data
    print("Test data")
    y_hat_svm_class = svm_class.predict(X_test)
    acc_svm_class = svm_class.score(X_test, y_test)
    print("Accuracy on test data = %f" % acc_svm_class)
    prec, recal, fscore, support = precision_recall_fscore_support(y_test,
                                                              y_hat_svm_class)
    print('precision: ', prec)
    print('recall: ', recal)
    print('fscore: ', fscore)
    print()