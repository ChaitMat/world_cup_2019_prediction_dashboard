import pandas as pd
import numpy as np
import sqlite3
import io

import dash_table

def getIndvData(excel_raw, data):

    df = pd.read_excel(io.BytesIO(excel_raw))

    upData = []

    upData.append(df.iloc[6,1].upper())

    upData.append(df.iloc[7,1].upper())

    league_pred = df.iloc[23:58, 2].reset_index(drop =True)
    df_league = pd.DataFrame(data[0])
    df_league['Predictions'] = league_pred
    league = df_league.to_dict('records')
    upData.append(league)

    semi_pred = df.iloc[69:71, 2].reset_index(drop =True)
    df_semi = pd.DataFrame(data[1])
    df_semi['Predictions'] = semi_pred
    semi = df_semi.to_dict('records')
    upData.append(semi)

    final_pred = df.iloc[77:78, 2].reset_index(drop =True)
    df_final = pd.DataFrame(data[2])
    df_final['Predictions'] = final_pred
    final = df_final.to_dict('records')
    upData.append(final)

    semiteam_pred = df.iloc[61:65, 1].reset_index(drop =True)
    df_semiteam = pd.DataFrame(data[3])
    df_semiteam['Predictions'] = semiteam_pred
    semiteam = df_semiteam.to_dict('records')
    upData.append(semiteam)

    players_pred = df.iloc[84:88, 1].reset_index(drop =True)
    df_players = pd.DataFrame(data[4])
    df_players['Predictions'] = players_pred
    players = df_players.to_dict('records')
    upData.append(players)

    return upData

    # table = dash_table.DataTable(
    #                             id='datatable-league-predictions',
    #                             data=,
    #                             columns=[{"name": i, "id": i} for i in dataTable[0].columns], 
    #                             editable=True,
    #                             style_cell_conditional =  styleCell,
    #                             style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
    #                             style_data_conditional = table_style,
    #                             style_header = table_header   
    #                             )


    # predictions.columns=['Match/Team/Player','Prediction']
    # s_predictions = predictions.reset_index(drop =True)
    # s_predictions.columns=['Match','Prediction']

    # semi = df.iloc[69:71,1:3]
    # semi.columns=['Match/Team/Player','Prediction']
    # predictions = predictions.append(semi)
    # s_semi = semi.reset_index(drop =True)
    # s_semi.columns=['Match','Prediction']

    # final = df.iloc[77:78,1:3]
    # final.columns=['Match/Team/Player','Prediction']
    # final['Match/Team/Player'] = 'Final'
    # predictions = predictions.append(final)
    # s_final = final.reset_index(drop =True)
    # s_final.columns=['Match','Prediction']

    # semi_teams = df.iloc[61:65,0:2]
    # semi_teams.columns=['Match/Team/Player','Prediction']
    # predictions = predictions.append(semi_teams)
    # s_semi_teams = semi_teams.reset_index(drop =True)
    # s_semi_teams.columns=['Team','Prediction']

    # players = df.iloc[84:88,0:2]
    # players.columns=['Match/Team/Player','Prediction']
    # predictions = predictions.append(players).reset_index(drop =True)
    # s_players = players.reset_index(drop =True)
    # s_players.columns=['Player','Prediction']

    # predictions['Points'] = np.nan

    # conn = sqlite3.connect('./database/predictions.sqlite')
    # emno = df.iloc[7,1].upper()
    # predictions.to_sql(emno, conn, if_exists= 'replace', index = False)
    # conn.close()
    
    # emName = df.iloc[6,1].upper()
    
    # to_send = [s_predictions, s_semi, s_final, s_semi_teams, s_players, emno, emName]
    
    # return to_send

