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

@app.callback(
              [
               Output('name', 'value'), Output('emno', 'value'),
               Output('datatable-league-predictions', 'data'),
               Output('datatable-semi-final-predictions', 'data'),
               Output('datatable-final-predictions', 'data'),
               Output('datatable-semi-final-teams-predictions', 'data'),
               Output('datatable-players-predictions', 'data'),
              ],
              [Input('upload-data', 'contents')],
              [State('datatable-league-predictions', 'data'),
              State('datatable-semi-final-predictions', 'data'),
              State('datatable-final-predictions', 'data'),
              State('datatable-semi-final-teams-predictions', 'data'),
              State('datatable-players-predictions', 'data'),
              State('upload-data', 'filename')])
              
def upload_data(excel, league, semi, final, semiTeam, players, filename):
    if league is not None:
        if excel is not None:
            content_type, content_string = excel.split(',')

            decoded = base64.b64decode(content_string)

            data = []

            data.append(league)
            data.append(semi)
            data.append(final)
            data.append(semiTeam)
            data.append(players)

            try:
                if 'xls' in filename:
                    updated_updated = getIndvData(decoded,data)

                    name= updated_updated[0]
                    emno = updated_updated[1]
                    upLeague = updated_updated[2]
                    upSemi = updated_updated[3]
                    upFinal = updated_updated[4]
                    upSemiTeam = updated_updated[5]
                    upPlayers = updated_updated[6]

                    return name, emno, upLeague, upSemi, upFinal, upSemiTeam, upPlayers

            except Exception as e:
                print(e)
                return '404'


           
    return league
    


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

