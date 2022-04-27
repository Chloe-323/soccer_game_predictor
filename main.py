import get_y
import get_x
import importing
import preprocessing
# import pca


def main():
    dfs=importing.get_all_tables('data/database.sqlite')
    dfs=preprocessing.filter_data(dfs)
    #for i in dfs["Team_Attributes"]:
    #    if dfs["Team_Attributes"][i].hasnans:
    #      print(dfs["Team_Attributes"][i].name)
    X = get_x.get_x(dfs)
    y = get_y.get_y(dfs)
    # unsupervised learning
    # X = pca.pca(X)

    # do logistic, svm, and neural network


if __name__==main():
    main()
