import datetime
import numpy as np

test = 0
home_player_start = 5 
away_player_start = 16
api_idx = 1


def team_vals(id):
    pass
def player_vals(id):
    pass


def age(date_of_match_strings, birthday_strings):
    match_d_split = i.split(" ")[0].split("-")
    birthday_d_split = i.split(" ")[0].split("-")
    match_dates = [datetime.date(int(i[0]), int(i[1]), int(i[2])) for i in
                   match_d_splits]
    birthday = [datetime.date(int(i[0]), int(i[1]), int(i[2])) for i in
                birthday_d_splits]
    return (match_dates[0] - birthday[0]).days

def get_player_attributes(np_players, np_player_attrs, player_id):
    to_ret = []
    for i in np_players:
        if i[1] == player_id:
            to_ret.extend(i[2:])
    for i in np_player_attrs:
        if i[1] == player_id:
            to_ret.extend(i[2:])
    return to_ret



def get_team_attributes(np_team_attr, team_id):
    #the ones we care about: 
    for i in np_team_attr:
        if i[1] == team_id:
            return i[2:]

def get_x(dfs):
    '''
    features: age, height, weight, 29 player attributes * 22 players

    :param dfs:
    :return:
        x:
            home_team:
                home_team_attributes
                home_players:
                    player_attributes
                    age
                    height
                    weight
            away_team:
                away_team_attributes
                away_players:
                    player_attributes
                    age
                    height
                    weight
    '''
    matches = np.array(dfs["Match"])
    players = np.array(dfs["Player"])
    player_attributes = np.array(dfs["Player_Attributes"])
    team_attributes = np.array(dfs["Team_Attributes"])
    x = []

    for i in matches:
        x_i = []
        #home team attributes
        x_i.append(get_team_attributes(team_attributes, i[2]))
        #home team players
        for j in i[home_player_start:away_player_start]:
            pa = get_player_attributes(players, player_attributes, j)
            pa[0] = age([i[0]], [pa[0]])[0]
            x_i.extend(pa)
        #away team attributes
        x_i.append(get_team_attributes(team_attributes, i[3]))
        for j in i[away_player_start:]:
            pa = get_player_attributes(players, player_attributes, j)
            pa[0] = age([i[0]], [pa[0]])[0]
            x_i.extend(pa)
        x.append(x_i)
    return np.array(x)
