import numpy as np


def filter_team_attributes(dfs):
    dfs=dfs.drop("team_fifa_api_id",1)
    dfs=dfs.drop("date",1)
    dfs= dfs.drop_duplicates(subset=["team_api_id"], keep='last')
    dfs["buildUpPlaySpeedClass"]=np.where(dfs["buildUpPlaySpeedClass"]
        =="Slow",0,np.where(dfs["buildUpPlaySpeedClass"]=="Balanced",1,2))
    # drop buildUpPlayDribbling as >1/2 of the entries are nan
    dfs.drop("buildUpPlayDribbling",1)

    dfs["buildUpPlayPositioningClass"] = np.where(dfs["buildUpPlayPositioningClass"]
                                              == "Organised", 0, 1)
    # drop because of value present, therefore redundant
    dfs.drop("buildUpPlayPassingClass",1)
    dfs.drop("chanceCreationPassingClass", 1)
    dfs.drop("chanceCreationCrossingClass", 1)
    dfs.drop("chanceCreationShootingClass", 1)
    dfs.drop("defencePressureClass", 1)
    dfs.drop("defenceAggressionClass", 1)
    dfs.drop("defenceTeamWidthClass", 1)

    dfs["chanceCreationPositioningClass"] = np.where(
        dfs["chanceCreationPositioningClass"] == "Organised", 0, 1)
    dfs["defenceDefenderLineClass"] = np.where(
        dfs["defenceDefenderLineClass"] == "Cover", 0, 1)

    return dfs


def filter_player_attributes(dfs):
    dfs = dfs.drop_duplicates(subset=["player_api_id"], keep='first')
    dfs=dfs.drop("player_fifa_api_id", 1)
    dfs=dfs.drop("date", 1)

    # drop because insufficient or undefined data
    has_nan=["attacking_work_rate",
    "volleys",
    "curve",
    "agility",
    "balance",
    "jumping",
    "vision",
    "defensive_work_rate",
    "sliding_tackle"]
    for i in has_nan:
        dfs = dfs.drop(i, 1)

    dfs["preferred_foot"] = np.where(dfs["preferred_foot"] == "left", 0, 1)


    return dfs

def filter_data(dfs):
    dfs["Team_Attributes"]=filter_team_attributes(dfs["Team_Attributes"])
    dfs["Player_Attributes"]=filter_player_attributes(dfs["Player_Attributes"])
    return dfs
