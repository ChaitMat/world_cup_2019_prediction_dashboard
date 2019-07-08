import pandas as pd
import sqlite3

from get_emno import getEmno
from get_name import getName

def updateRank():

    nameList = getName()
    emnoList = getEmno()

    conn1 = sqlite3.connect("./database/score.sqlite")
    score = pd.read_sql_query("SELECT * FROM scores", conn1)

    conn2 =  sqlite3.connect("./database/predictions.sqlite")
    

    for i,j in zip(emnoList, nameList):

        predictions = pd.read_sql_query("SELECT * FROM "+i, conn2)

        emnoName = i+':'+j
        score[emnoName] = predictions["Points"].sum() 
    
    score.to_sql('scores', conn1, if_exists= 'replace', index = False)
    conn1.close()
    conn2.close()
