import base64

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas


from app import app
from get_individual_data import getIndvData

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
            
        return html.Div([
                html.H3('Check predictions and submit.'),
                html.H5('Name: '+ dataTable[6], id = 'emp-name'),
                html.H5('EM No.: ' + dataTable[5], id = 'emp-id'),
                html.Div([
                        html.Div([
                                
                            html.Div([
                                html.Div([
                                    html.Div([
                                            html.H3('League Matches'),
                                            dash_table.DataTable(
                                            id='datatable-league-predictions',
                                            data=dataTable[0].to_dict('records'),
                                            columns=[{"name": i, "id": i} for i in dataTable[0].columns], 
                                            editable=False,
                                            style_table={'maxWidth': '300px'},
                                            style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'}
                                            )
                                        ],className = "card-content")
                                    ], className = "card")
                            ], className="col l4"),
                                            
                                            
                             html.Div([
                                    html.Div([
                                        html.Div([
                                                html.H3('Semi Finals'),
                                                dash_table.DataTable(
                                                id='datatable-semi-final-predictions',
                                                data=dataTable[1].to_dict('records'),
                                                columns=[{"name": i, "id": i} for i in dataTable[1].columns], 
                                                editable=False,
                                                style_table={'maxWidth': '300px'},
                                                style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'}
                                                ),
                                                
                                                html.H3('Finals'),
                                                dash_table.DataTable(
                                                id='datatable-semi-final-predictions',
                                                data=dataTable[2].to_dict('records'),
                                                columns=[{"name": i, "id": i} for i in dataTable[2].columns], 
                                                editable=False,
                                                style_table={'maxWidth': '300px'},
                                                style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'}
                                                ),
                                                
                                                html.H3('Semi Final Teams'),
                                                dash_table.DataTable(
                                                id='datatable-semi-final-predictions',
                                                data=dataTable[3].to_dict('records'),
                                                columns=[{"name": i, "id": i} for i in dataTable[3].columns], 
                                                editable=False,
                                                style_table={'maxWidth': '300px'},
                                                style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'}
                                                ),
                                                
                                                html.H3('Players'),
                                                dash_table.DataTable(
                                                id='datatable-semi-final-predictions',
                                                data=dataTable[4].to_dict('records'),
                                                columns=[{"name": i, "id": i} for i in dataTable[4].columns], 
                                                editable=False,
                                                style_table={'maxWidth': '300px'},
                                                style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'}
                                                ),
                                                
                                                html.H3('Submit Predictions'),
                                                html.P('Check your predicions and hit submit.'),
                                                html.P('Each employee can only submit their predictions only once.'),
                                                html.Button('Submit', id='submit-button', type = 'submit'),
                                                
                                            ],className = "card-content")
                                        ], className = "card")
                                ], className="col l4"),
                        
                        
                        ], className="row")
                    ])
                ])
    

