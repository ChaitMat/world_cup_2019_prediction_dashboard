import base64

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas
from urllib.parse import parse_qs

from app import app
from get_individual_data import getIndvData
from calculate_score import calculate_score
from display_individual_data import dispIndvData
from layouts import showData, uploadShowData

@app.callback(Output('datatable-league-predictions', 'data'),
              [Input('upload-data', 'contents')],
              [State('datatable-league-predictions', 'data'),
              State('upload-data', 'filename')])
              
def upload_data(excel, table_league, filename):
    if table_league is not None:
        if excel is not None:
            content_type, content_string = excel.split(',')

            decoded = base64.b64decode(content_string)


            try:
                if 'xls' in filename:
                    print(table_league)

            except Exception as e:
                print(e)
                return '404'

            # link = "/submit/name="+ dataTable[6]+'&emno='+dataTable[5]

            # uploadDataLayout = uploadShowData(dataTable, link)
                
    return table_league
    


def submit(pathname):
    data = (pathname).split('/')[2]
    name = parse_qs(data)['name'][0]
    emno = parse_qs(data)['emno'][0]
    
    score = calculate_score(emno, name)

    dataTable = dispIndvData(emno)

    showDataLayout = showData(dataTable,name,emno,int(score))


    return showDataLayout


@app.callback(
    dash.dependencies.Output('your-score-container', 'children'),
    [dash.dependencies.Input('your-score-dropdown', 'value')])
def yourPredictions(value):

    if value != None:

        emno = value.split(':')[0]  
        name = value.split(':')[1]  

        score = calculate_score(emno, name)

        dataTable = dispIndvData(emno)

        showDataLayout = showData(dataTable,name,emno,int(score))

        return showDataLayout

