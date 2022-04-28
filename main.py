import get_y
import get_x
import importing
import filter_data
import pca
import preprocess


def main():
    dfs=importing.get_all_tables('data/database.sqlite')
    dfs=filter_data.filter_data(dfs)

    X = get_x.get_x(dfs)
    y = get_y.get_y(dfs)

    # normalizing stuff, split into test and train sets
    X_train, X_test, y_train, y_test=preprocess.preprocess(X,y)

    # unsupervised learning
    X = pca.pca(X)

    # do logistic, svm, and neural network; try different feature transformation
    # and different regularization techniques, and graph them; table of results




if __name__==main():
    main()
