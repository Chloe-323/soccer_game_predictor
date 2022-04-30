import numpy as np
from sklearn.preprocessing import OneHotEncoder

def get_y(dfs):
    '''
    Assign home win to be 0; draw be 0.5; away win be 1
    :param dfs:
    :return: y: np.array
    '''

    home_goals=dfs["Match"]["home_team_goal"]
    away_goals=dfs["Match"]["away_team_goal"]

    y=np.where(home_goals>away_goals,0,(np.where(home_goals==away_goals,.5,1)))

    return y

def get_y_one_hot(dfs):
    '''
    one hot encoding for y. first column: home win; second column: draw
    ; third column: away win
    :param dfs:
    :return: y:np.array
    '''
    y=get_y(dfs)
    y=y.reshape((len(y),1))
    enc=OneHotEncoder()
    enc.fit(y)
    y=enc.transform(y).toarray()
    return y