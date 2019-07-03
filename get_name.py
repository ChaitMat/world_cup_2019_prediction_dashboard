import pandas as pd
import sqlite3

def getName():

    conn = sqlite3.connect("./database/score.sqlite")
    df = pd.read_sql_query("SELECT * FROM scores", conn)
    df = df.T
    df.reset_index(inplace= True)
    temp = df['index'].str.split(":", n=1, expand = True)
    name = temp[1].tolist()

    return name