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

    y=np.where(home_goals>away_goals,0,(np.where(home_goals==away_goals,.5,1)))

    return y
