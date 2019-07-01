import pandas as pd
import sqlite3

def dispIndvData(emno):

    conn = sqlite3.connect("./database/predictions.sqlite")

    df = pd.read_sql_query("SELECT * FROM "+emno, conn)

    league= df.iloc[:35].reset_index(drop =True)
    league.columns=['Match','Prediction','Points']
 
    semi = df.iloc[35:37]
    semi.columns=['Match','Prediction','Points']
  
    final = df.iloc[37:38]
    final.columns=['Match','Prediction','Points']

    semi_teams = df.iloc[38:42]
    semi_teams.columns=['Team','Prediction','Points']

    players = df.iloc[42:]
    players.columns=['Player','Prediction','Points']

    conn.close()

    to_send = [league,semi,final,semi_teams,players]
    
    return to_send

