import pandas as pd
import sqlite3

pd.options.mode.chained_assignment = None

def get_rank_table():
    conn = sqlite3.connect("./database/score.sqlite")
    df = pd.read_sql_query("SELECT * FROM scores", conn)
    df = df.T
    df.reset_index(inplace= True)
    temp = df['index'].str.split(":", n=1, expand = True)
    df['EMNO'] = temp[0]
    df['Name'] = temp[1]
    df.drop(['index'], axis = 1, inplace = True)
    df = df[['EMNO', 'Name', 0]]
    df.columns = ['EMNO', 'Name', 'Score']
    df['Rank'] = df['Score'].rank(ascending = False, method ='dense')
    df.sort_values('Rank', inplace = True)
    df['Rank'] = df['Rank'].astype('int', copy =False)
    df = df.reset_index(drop =True)
    conn.close()
    return df

