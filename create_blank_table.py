import pandas as pd
import sqlite3

def createBlanktable():

    conn = sqlite3.connect('./database/base_table.sqlite')
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    tables = cursorObj.fetchall()

    table = []
    for i in tables:
        df = pd.read_sql_query("SELECT * FROM "+i[0], conn)
        df['Predictions'] = ""

        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])


        table.append(df)



    conn.close()


    return table

