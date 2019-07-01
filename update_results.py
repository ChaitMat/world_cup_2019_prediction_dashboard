import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

from get_emno import getEmno
from update_points import updatePoints

def updateResults():

    page = requests.get('https://www.cricbuzz.com/cricket-series/2697/icc-cricket-world-cup-2019/matches')
    cricPage = BeautifulSoup(page.content, 'html.parser')
    resultTable = cricPage.find_all(class_ = 'cb-text-complete')
    resultList = []

    for match in resultTable:
        row = list(match.children)[0]
            
        if 'won' in row:
            resultDict = {}
            textSplit = row.split("won")
            resultDict['Result'] = textSplit[0].rstrip()
            resultList.append(resultDict)
            
        elif 'abandoned' or 'No result' in row:
            resultDict = {}
            resultDict['Result'] = 'NR'
            resultList.append(resultDict)

    df = pd.DataFrame(resultList)
    updated_results = df[10:].reset_index(drop =True)
    conn = sqlite3.connect('./database/results.sqlite')
    updated_results.to_sql("results", conn, if_exists= 'replace', index = False)
    conn.close()

    emno = getEmno()

    for i in emno:
        updatePoints(i)

