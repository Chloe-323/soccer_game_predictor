import importing
import numpy as np

def get_y(dfs):
    '''
    Assign home win to be 0; draw be 0.5; away win be 1
    :param dfs:
    :return: y: np.array
    '''

    home_goals=dfs["Match"]["home_team_goal"]
    away_goals=dfs["Match"]["away_team_goal"]

    y=np.zeros((len(home_goals),))

    for i in range(len(home_goals)):
        if home_goals[i]==away_goals[i]:
            y[i]=0.5
        elif home_goals[i]>away_goals[i]:
            y[i]=0
        else:
            y[i]=1
    return y
