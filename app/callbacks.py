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

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename')])
def upload_data(contents, filename):
    if contents is not None:
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)

        try:
            if 'xls' in filename:
                dataTable = getIndvData(decoded)

        except Exception as e:
            print(e)
            return '404'

        link = "/submit/name="+ dataTable[6]+'&emno='+dataTable[5]

        uploadDataLayout = uploadShowData(dataTable, link)
            
        return uploadDataLayout
    


def submit(pathname):
    data = (pathname).split('/')[2]
    name = parse_qs(data)['name'][0]
    emno = parse_qs(data)['emno'][0]
    
    score = calculate_score(emno)

    dataTable = dispIndvData(emno)

    showDataLayout = showData(dataTable,name,emno,int(score))


    return showDataLayout

