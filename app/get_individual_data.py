import pandas as pd
import numpy as np
import sqlite3
import io

def getIndvData(excel_raw):

    df = pd.read_excel(io.BytesIO(excel_raw))

    predictions= df.iloc[23:58, 1:3].reset_index(drop =True)
    predictions.columns=['Match/Team/Player','Prediction']
    s_predictions = predictions.reset_index(drop =True)
    s_predictions.columns=['Match','Prediction']

    semi = df.iloc[69:71,1:3]
    semi.columns=['Match/Team/Player','Prediction']
    predictions = predictions.append(semi)
    s_semi = semi.reset_index(drop =True)
    s_semi.columns=['Match','Prediction']

    final = df.iloc[77:78,1:3]
    final.columns=['Match/Team/Player','Prediction']
    final['Match/Team/Player'] = 'Final'
    predictions = predictions.append(final)
    s_final = final.reset_index(drop =True)
    s_final.columns=['Match','Prediction']

    semi_teams = df.iloc[61:65,0:2]
    semi_teams.columns=['Match/Team/Player','Prediction']
    predictions = predictions.append(semi_teams)
    s_semi_teams = semi_teams.reset_index(drop =True)
    s_semi_teams.columns=['Team','Prediction']

    players = df.iloc[84:88,0:2]
    players.columns=['Match/Team/Player','Prediction']
    predictions = predictions.append(players).reset_index(drop =True)
    s_players = players.reset_index(drop =True)
    s_players.columns=['Player','Prediction']

    predictions['Points'] = np.nan

    conn = sqlite3.connect('./database/predictions.sqlite')
    emno = df.iloc[7,1].upper()
    predictions.to_sql(emno, conn, if_exists= 'replace', index = False)
    conn.close()
    
    emName = df.iloc[6,1].upper()
    
    to_send = [s_predictions, s_semi, s_final, s_semi_teams, s_players, emno, emName]
    
    return to_send

