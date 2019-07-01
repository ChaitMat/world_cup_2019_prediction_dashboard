import pandas as pd
import sqlite3


def updateScore(emno):
    conn1 =  sqlite3.connect("./database/predictions.sqlite")
    predictions = pd.read_sql_query("SELECT * FROM "+emno, conn1) 
    conn2 =  sqlite3.connect("./database/results.sqlite")
    results = pd.read_sql_query("SELECT * FROM results", conn2)
    result = results['Result']
    predict = predictions['Prediction']
    for i in range(result.size):
        if result[i] == 'NR':
            predictions['Points'][i] = 5
        elif result[i].strip().lower() == predict[i].strip().lower():
            predictions['Points'][i] = 10
        else:
            predictions['Points'][i] = 0
    predictions.to_sql(emno, conn1, if_exists= 'replace', index = False)  
    conn1.close()
    conn2.close()