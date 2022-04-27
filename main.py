import get_y
import get_x
import importing
# import pca


def main():
    dfs=importing.get_all_tables('data/database.sqlite')
    X = get_x.get_x(dfs)
    y = get_y.get_y(dfs)
    # unsupervised learning
    # X = pca.pca(X)

    # do logistic, svm, and neural network


if __name__==main():
    main()
