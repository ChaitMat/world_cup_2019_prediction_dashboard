
# Code sraps the match results from the web and stores it in a sqlite database

# In[11]:


import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3


# In[2]:


page = requests.get('https://www.standard.co.uk/sport/cricket/cricket-world-cup-2019-results-and-standings-full-table-for-tournament-group-stage-a4174011.html')


# In[3]:


cricPage = BeautifulSoup(page.content, 'html.parser')


# In[4]:


resultTable = cricPage.find_all('table')[1].find_all('tr')


# In[5]:


resultList = []

for match in resultTable:
    row = list(match.children)
    resultStr = list(row[1].children)
    dateStr= list(row[3].children)
    if type(resultStr[0]) == bs4.element.Tag:
        resultText = resultStr[0].get_text()       
    else:
        resultText = resultStr[0]
        
   
        
    if type(dateStr[0]) == bs4.element.Tag:
        dateText = (dateStr[0].get_text()) + ' 2019 00:00:00'
    else: 
        dateText = (dateStr[0]) + ' 2019 00:00:00'
        
        
        
    if 'bt' in resultText:
        resultDict = {}
        textSplit = resultText.split("bt")
        resultDict['Date'] = dateText
        resultDict['Result'] = textSplit[0].rstrip()
        resultList.append(resultDict)
        
    elif 'vs' and '(Rained off)' in resultText:
        resultDict = {}
        resultDict['Date'] = dateText
        resultDict['Result'] = 'NR'
        resultList.append(resultDict)


# In[6]:


df = pd.DataFrame(resultList)


# In[7]:


df['Date'] = pd.to_datetime(df['Date'])


# In[8]:


updated_results = df[df['Date'] > '2019-06-06'].reset_index(drop =True)


# In[12]:


conn = sqlite3.connect('./database/results.sqlite')


# In[13]:


updated_results.to_sql("results", conn, if_exists= 'replace', index = False)


# In[14]:


conn.close()

