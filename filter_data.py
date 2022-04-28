import numpy as np


def filter_team_attributes(dfs):
    dfs = dfs.drop("team_fifa_api_id", 1)
    dfs = dfs.drop("date", 1)
    dfs = dfs.drop_duplicates(subset=["team_api_id"], keep='last')
    dfs["buildUpPlaySpeedClass"] = np.where(dfs["buildUpPlaySpeedClass"]
                                            == "Slow", 0, np.where(
        dfs["buildUpPlaySpeedClass"] == "Balanced", 1, 2))
    # drop buildUpPlayDribbling as >1/2 of the entries are nan
    dfs=dfs.drop("buildUpPlayDribbling", 1)

    dfs["buildUpPlayDribblingClass"] = np.where(dfs["buildUpPlayDribblingClass"]
                                            == "Little", 0, np.where(
        dfs["buildUpPlayDribblingClass"] == "Normal", 1, 2))

    dfs["buildUpPlayPositioningClass"] = np.where(
        dfs["buildUpPlayPositioningClass"]
        == "Organised", 0, 1)
    # drop because of value present, therefore redundant
    dfs=dfs.drop(["buildUpPlayPassingClass","chanceCreationPassingClass",
        "chanceCreationCrossingClass", "chanceCreationShootingClass",
        "defencePressureClass", "defenceAggressionClass",
        "defenceTeamWidthClass"],1)

    dfs["chanceCreationPositioningClass"] = np.where(
        dfs["chanceCreationPositioningClass"] == "Organised", 0, 1)
    dfs["defenceDefenderLineClass"] = np.where(
        dfs["defenceDefenderLineClass"] == "Cover", 0, 1)

    return dfs


def filter_player_attributes(dfs):
    dfs = dfs.drop_duplicates(subset=["player_api_id"], keep='first')
    dfs = dfs.drop("player_fifa_api_id", 1)
    dfs = dfs.drop("date", 1)

    # drop because insufficient or undefined data
    has_nan = ["attacking_work_rate",
               "volleys",
               "curve",
               "agility",
               "balance",
               "jumping",
               "vision",
               "defensive_work_rate",  # this column has full but weird inputs
               "sliding_tackle"]
    for i in has_nan:
        dfs = dfs.drop(i, 1)

    dfs["preferred_foot"] = np.where(dfs["preferred_foot"] == "left", 0, 1)

    return dfs


def filter_match(dfs):
    dfs = dfs[["id", "date", "home_team_api_id", "away_team_api_id",
              "home_team_goal", "away_team_goal","home_player_1",
              "home_player_2","home_player_3","home_player_4","home_player_5",
              "home_player_6","home_player_7","home_player_8","home_player_9",
              "home_player_10","home_player_11","away_player_1","away_player_2"
              ,"away_player_3","away_player_4","away_player_5","away_player_6"
              ,"away_player_7","away_player_8","away_player_9","away_player_10","away_player_11"]]
    dfs=dfs.dropna()
    return dfs


def filter_data(dfs):
    dfs["Player"] = dfs["Player"].drop('player_name', 1)
    dfs["Player"] = dfs["Player"].drop('player_fifa_api_id', 1)

    dfs["Match"]=filter_match(dfs["Match"])
    dfs["Team_Attributes"] = filter_team_attributes(dfs["Team_Attributes"])
    dfs["Player_Attributes"] = filter_player_attributes(
        dfs["Player_Attributes"])

    return dfs
