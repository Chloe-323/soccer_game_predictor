import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import IPython

def import_from_sqlite(db_name, table_name):
    '''
    Imports data from SQLite database
    '''
    df = pd.read_sql_query("SELECT * FROM {}".format(table_name), "sqlite:///" + db_name)
    return df

def get_table_names(db_name):
    '''
    Returns a list of all table names in the database
    '''
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = [table_name[0] for table_name in c.fetchall()]
    return table_names

def get_all_tables(db_name):
    '''
    Returns a dataframe for all tables in the database
    '''
    dataframes = {table_name : import_from_sqlite(db_name, table_name) for table_name in get_table_names(db_name)}
    return dataframes

def print_data():
    print("Loading data...")
    dfs = get_all_tables('data/database.sqlite')
    print("Data loaded.")
    print("\n")
    for i in dfs:
        print(i, ":", dfs[i].shape)
        for j in dfs[i]:
            print("\t", j, ":", dfs[i][j].dtype)

