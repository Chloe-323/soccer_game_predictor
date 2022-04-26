import importing
import numpy as np

def get_y(dfs):
    home_goals=dfs["Match"]["home_team_goal"]
    away_goals=dfs["Match"]["away_team_goal"]
    print(home_goals-away_goals>0)
get_y(importing.get_all_tables('data/database.sqlite'))