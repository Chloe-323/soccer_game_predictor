import datetime

def team_vals(id):
    pass
def player_vals(id):
    pass


def age(date_of_match_strings, birthday_strings):
    match_d_splits = [i.split(" ")[0].split("-") for i in
                      date_of_match_strings]
    birthday_d_splits = [i.split(" ")[0].split("-") for i in
                         birthday_strings]
    match_dates = [datetime.date(int(i[0]), int(i[1]), int(i[2])) for i in
                   match_d_splits]
    birthday = [datetime.date(int(i[0]), int(i[1]), int(i[2])) for i in
                birthday_d_splits]
    return (match_dates[0] - birthday[0]).days

def get_player_attributes(dfs, player_id):
    desired_attributes = [
            "overall_rating",
            "potential",
            "preferred_foot",
            "attacking_work_rate",
            "defensive_work_rate",
            "crossing",
            "finishing",
            "heading_accuracy",
            "short_passing",
            "volleys",
            "dribbling",
            "curve",
            "free_kick_accuracy",
            "long_passing",
            "ball_control",
            "acceleration",
            "sprint_speed",
            "agility",
            "reactions",
            "balance",
            "shot_power",
            "jumping",
            "stamina",
            "strength",
            "long_shots",
            "aggression",
            "interceptions",
            "positioning",
            "vision",
            "penalties",
            "marking",
            "standing_tackle",
            "sliding_tackle",
            "gk_diving",
            "gk_handling",
            "gk_kicking",
            "gk_positioning",
            "gk_reflexes"
        ]
    to_ret = {}
    for i in range(len(dfs["Player"])):
        if dfs["Player"]["player_api_id"][i] == player_id:
            to_ret["birthday"] = dfs["Player"]["birthday"][i]
            to_ret["height"] = dfs["Player"]["height"][i]
            to_ret["weight"] = dfs["Player"]["weight"][i]
    for i in range(len(dfs["Player_Attributes"])):
        if dfs["Player_Attributes"]["player_api_id"][i] == player_id:
            for j in desired_attributes:
                to_ret[j] = dfs["Player_Attributes"][j][i]
    return to_ret


def get_players(dfs, match_id):
    players = []
    for i in range(1, 12):
        players.append(dfs["Match"]["home_player_" + str(i)][match_id])
    for i in range(1, 12):
        players.append(dfs["Match"]["away_player_" + str(i)][match_id])
    return players


def get_team_attributes(dfs, team_id):
    for i in range(len(dfs["Team_Attributes"])):
        if dfs["Team_Attributes"]["team_api_id"][i] == team_id:
            to_ret = []
            desired_attributes = [
                    "buildUpPlaySpeed",
                    "buildUpPlayDribbling",
                    "buildUpPlayPassing",
                    "chanceCreationPassing",
                    "chanceCreationCrossing",
                    "chanceCreationShooting",
                    "defencePressure",
                    "defenceAggression",
                    "defenceTeamWidth"
                    ]
            for j in desired_attributes:
                to_ret.append(dfs["Team_Attributes"][j][i])
            return to_ret

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
    x = []
    for i in range(len(dfs["Match"])):
        x_i = []
        date_of_match = dfs["Match"]["date"][i]
        players = get_players(dfs, i)
        #home team attributes
        home_team_attributes = get_team_attributes(dfs, dfs["Match"]["home_team_api_id"][i])
        x_i.extend(home_team_attributes)
        #home players
        for player in players[:11]:
            player_attributes = get_player_attributes(dfs, player)
            player_attributes["age"] = age(dfs["Match"]["date"][i], player_attributes["birthday"])
            player_attributes.pop("birthday")
        #away team attributes
        away_team_attributes = get_team_attributes(dfs, dfs["Match"]["away_team_api_id"][i])
        x_i.extend(away_team_attributes)
        #away players
        for player in players[11:]:
            player_attributes = get_player_attributes(dfs, player)
            player_attributes["age"] = age(dfs["Match"]["date"][i], player_attributes["birthday"])
            player_attributes.pop("birthday")
            for k, v in player_attributes.items():
                x_i.append(v)
        x.append(x_i)
    return x
