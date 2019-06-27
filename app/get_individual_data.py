import pandas as pd
import numpy as np
import sqlite3
import io

def getIndvData(excel_raw):

    df = pd.read_excel(io.BytesIO(excel_raw))

    predictions= df.iloc[23:58, 1:3].reset_index(drop =True)
    predictions.columns=['Match/Team/Player','Prediction']

    semi = df.iloc[69:71,1:3]
    semi.columns=['Match/Team/Player','Prediction']
    predictions = predictions.append(semi)

    final = df.iloc[77:78,1:3]
    final.columns=['Match/Team/Player','Prediction']
    final['Match/Team/Player'] = 'Final'
    predictions = predictions.append(final)

    semi_teams = df.iloc[61:65,0:2]
    semi_teams.columns=['Match/Team/Player','Prediction']
    predictions = predictions.append(semi_teams)

    players = df.iloc[84:88,0:2]
    players.columns=['Match/Team/Player','Prediction']
    predictions = predictions.append(players).reset_index(drop =True)

    predictions['Points'] = np.nan

    conn = sqlite3.connect('./database/predictions.sqlite')
    emno = df.iloc[7,1].upper()
    predictions.to_sql(emno, conn, if_exists= 'replace', index = False)
    conn.close()

