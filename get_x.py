import datetime
import numpy as np
import json
import time

home_player_start = 6 
away_player_start = 17
api_idx = 1


def team_vals(id):
    pass
def player_vals(id):
    pass


def age(date_of_match_strings, birthday_strings):
    dom_splits = date_of_match_strings.split(" ")[0].split("-")
    bd_splits = birthday_strings.split(" ")[0].split("-")
    dom = datetime.date(int(dom_splits[0]), int(dom_splits[1]), int(dom_splits[2]))
    bd = datetime.date(int(bd_splits[0]), int(bd_splits[1]), int(bd_splits[2]))
    return (dom - bd).days

def get_player_attributes(np_players, np_player_attrs, player_id):
    to_ret = []
    for i in np_players:
        if i[1] == player_id:
            to_ret.extend(i[2:])
    for i in np_player_attrs:
        if i[1] == player_id:
            to_ret.extend(i[2:])
    return to_ret



class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

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

    iterator = 0
    skipped = 0
    skipped_indices = []
    timer = time.monotonic()
    f = open("stuff.json", "w")
    for i in matches:
        iterator += 1
        if iterator % 50 == 0:
            print(iterator, ":", str(time.monotonic() - timer)[:5], "seconds")
        x_i = []
        #home team attributes
        try:
            x_i.extend(get_team_attributes(team_attributes, i[2]))
            #home team players
            for j in i[home_player_start:away_player_start]:
                pa = get_player_attributes(players, player_attributes, j)
                pa[0] = age(i[1], pa[0])
                x_i.extend(pa)
            #away team attributes
            x_i.extend(get_team_attributes(team_attributes, i[3]))
            for j in i[away_player_start:]:
                pa = get_player_attributes(players, player_attributes, j)
                pa[0] = age(i[1], pa[0])
                x_i.extend(pa)
            x.append(x_i)
            strn = json.dumps(x_i, cls=NpEncoder)
            f.write(strn + "\n")
        except:
            skipped += 1
            skipped_indices.append(iterator)
            print(i)
        #write to file
    f.close()
    print("skipped", skipped)
    print("skipped indices", skipped_indices)
    with open("skipped.txt", "w") as f:
        f.write(str(skipped_indices))
    return np.array(x)
