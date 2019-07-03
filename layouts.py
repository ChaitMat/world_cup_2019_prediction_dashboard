import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.graph_objs as go

from get_rank import get_rank_table
from get_graph_data import getGraphData
from create_blank_table import createBlanktable

def uploadLayout():

    dataTable = createBlanktable()


    table_style = [

                     {
                        'if' : {'row_index': 'odd'},
                        'backgroundColor': 'rgb(183,238,255)'
                    },

                   ]

    table_header = {'backgroundColor': 'rgb(248,248,248)', 'fontWeight': 'bold'}

    styleCell=[
        {'if': {'column_id': 'Predictions'},
         'width': '50%'}
    ]


    upload_layout = html.Div(children = [
         html.Div([
            html.Div([
                html.Div([
                        
                    html.Div([
                        html.Div([
                            html.Div([

                                html.H3(children='Upload Data'), 
                                html.H5(children='Upload your excel sheet or enter your predictions manually in the table below.'), 
                                html.P(children='Upload the completely filled excel file.(Only *xls/*xlxs files)'),

                            ],className = "card-content")
                        ], className = "card")
                    ], className="col l12"),
                ], className="row")
            ])
        
        ], id='output-data-upload'),

        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            
            multiple=False
        ),

        html.Div([

            html.Div([
                html.Div([
                    html.Div([
                            
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.H5('Enter your name'),
                                    dcc.Input(id='name', type='text'),
                                    html.H5('Enter your employee no.(Ex.: EM310)'),
                                    dcc.Input(id='emno', type='text'),
                                ],className = "card-content")
                            ], className = "card")
                        ], className="col l12"),
                    ], className="row")
                ])
            
            ]),



            html.Div([
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
                                        editable=True,
                                        style_cell_conditional =  styleCell,
                                        style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                        style_data_conditional = table_style,
                                        style_header = table_header   
                                        )
                                    ],className = "card-content")
                                ], className = "card")
                        ], className="col l6"),
                                        
                                                        
                        html.Div([
                                html.Div([
                                    html.Div([
                                        html.H3('Semi Finals'),
                                        dash_table.DataTable(
                                        id='datatable-semi-final-predictions',
                                        data=dataTable[1].to_dict('records'),
                                        columns=[{"name": i, "id": i} for i in dataTable[1].columns], 
                                        editable=True,
                                        style_cell_conditional =  styleCell,
                                        style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                        style_data_conditional = table_style,
                                        style_header = table_header   
                                        ),
                                        
                                        html.H3('Finals'),
                                        dash_table.DataTable(
                                        id='datatable-semi-final-predictions',
                                        data=dataTable[2].to_dict('records'),
                                        columns=[{"name": i, "id": i} for i in dataTable[2].columns], 
                                        editable=True,
                                        style_cell_conditional =  styleCell,
                                        style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                        style_data_conditional = table_style,
                                        style_header = table_header   
                                        ),
                                        
                                        html.H3('Semi Final Teams'),
                                        dash_table.DataTable(
                                        id='datatable-semi-final-predictions',
                                        data=dataTable[3].to_dict('records'),
                                        columns=[{"name": i, "id": i} for i in dataTable[3].columns], 
                                        editable=True,
                                        style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                        style_data_conditional = table_style,
                                        style_header = table_header   
                                        ),
                                        
                                        html.H3('Players'),
                                        dash_table.DataTable(
                                        id='datatable-semi-final-predictions',
                                        data=dataTable[4].to_dict('records'),
                                        columns=[{"name": i, "id": i} for i in dataTable[4].columns], 
                                        editable=True,
                                        style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                        style_data_conditional = table_style,
                                        style_header = table_header   
                                        ),
                                        
                                        # html.H3('Submit Predictions'),
                                        # html.P('Check your predicions and hit submit.'),
                                        # html.P('Each employee can only submit their predictions only once.'),
                                        # html.Button(dcc.Link("Submit", href=link), id='submit-button')
                                        
                                    ],className = "card-content")
                                ], className = "card")
                        ], className="col l6"),
                    ], className="row")
                ])
            
            ]),
        ], id='output-data-upload'),
    ])

    

    
    return upload_layout
 

def uploadShowData(dataTable,link):


    table_style = [

                     {
                        'if' : {'row_index': 'odd'},
                        'backgroundColor': 'rgb(183,238,255)'
                    },

                   ]

    table_header = {'backgroundColor': 'rgb(248,248,248)', 'fontWeight': 'bold'}

    upload_show_data = html.Div([html.Div([
                                    html.Div([
                        html.H3('Check predictions and submit.'),
                        html.H5('Name: '+ dataTable[6], id = 'emp-name'),
                        html.H5('EM No.: ' + dataTable[5], id = 'emp-id'),
                                    ],className = "card-content"),
                                ],className = "card"),
                        html.Div([
                                html.Div([
                                        
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                    html.H3('League Matches'),
                                                    dash_table.DataTable(
                                                    # id='datatable-league-predictions',
                                                    data=dataTable[0].to_dict('records'),
                                                    columns=[{"name": i, "id": i} for i in dataTable[0].columns], 
                                                    editable=False,
                                                    style_table={'maxWidth': '300px'},
                                                    style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                                    style_data_conditional = table_style,
                                                    style_header = table_header   
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
                                                        style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                                        style_data_conditional = table_style,
                                                        style_header = table_header   
                                                        ),
                                                        
                                                        html.H3('Finals'),
                                                        dash_table.DataTable(
                                                        id='datatable-semi-final-predictions',
                                                        data=dataTable[2].to_dict('records'),
                                                        columns=[{"name": i, "id": i} for i in dataTable[2].columns], 
                                                        editable=False,
                                                        style_table={'maxWidth': '300px'},
                                                        style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                                        style_data_conditional = table_style,
                                                        style_header = table_header   
                                                        ),
                                                        
                                                        html.H3('Semi Final Teams'),
                                                        dash_table.DataTable(
                                                        id='datatable-semi-final-predictions',
                                                        data=dataTable[3].to_dict('records'),
                                                        columns=[{"name": i, "id": i} for i in dataTable[3].columns], 
                                                        editable=False,
                                                        style_table={'maxWidth': '300px'},
                                                        style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                                        style_data_conditional = table_style,
                                                        style_header = table_header   
                                                        ),
                                                        
                                                        html.H3('Players'),
                                                        dash_table.DataTable(
                                                        id='datatable-semi-final-predictions',
                                                        data=dataTable[4].to_dict('records'),
                                                        columns=[{"name": i, "id": i} for i in dataTable[4].columns], 
                                                        editable=False,
                                                        style_table={'maxWidth': '300px'},
                                                        style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                                        style_data_conditional = table_style,
                                                        style_header = table_header   
                                                        ),
                                                        
                                                        html.H3('Submit Predictions'),
                                                        html.P('Check your predicions and hit submit.'),
                                                        html.P('Each employee can only submit their predictions only once.'),
                                                        html.Button(dcc.Link("Submit", href=link), id='submit-button')
                                                        
                                                    ],className = "card-content")
                                                ], className = "card")
                                        ], className="col l4"),
                                ], className="row")
                            ])
                        ])

    return upload_show_data
    



def showData(dataTable, name, emno, score):

    table_style = [

                     {
                        'if' : {'row_index': 'odd'},
                        'backgroundColor': 'rgb(183,238,255)'
                    },

                    {
                        'if':{
                            'column_id': 'Points',
                            'filter_query': '{Points} eq 0'
                        },

                        'backgroundColor': '#ff4c4c',
                        'color' : 'white'
                    },
                   ]

    table_header = {'backgroundColor': 'rgb(248,248,248)', 'fontWeight': 'bold'}
    
    showDataLayout = html.Div([html.Div([
                                    html.Div([
                html.H3('Current score'),
                html.H5('Name: '+ name, id = 'emp-name'),
                html.H5('EM No.: ' + emno, id = 'emp-id'),
                html.H3('Your current score: '+str(score)),
                                 ],className = "card-content"),
                            ],className = "card"),
                html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Div([
                                            html.H3('League Matches'),
                                            dash_table.DataTable(
                                            data=dataTable[0].to_dict('records'),
                                            columns=[{"name": i, "id": i} for i in dataTable[0].columns], 
                                            editable=False,
                                            style_table={'maxWidth': '300px'},
                                            style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                            style_data_conditional = table_style,
                                            style_header = table_header         
                                            )
                                        ],className = "card-content")
                                    ], className = "card")
                             ], className="col l6"),
                                            
                                            
                             html.Div([
                                    html.Div([
                                        html.Div([
                                                html.H3('Semi Finals'),
                                                dash_table.DataTable(
                                                data=dataTable[1].to_dict('records'),
                                                columns=[{"name": i, "id": i} for i in dataTable[1].columns], 
                                                editable=False,
                                                style_table={'maxWidth': '300px'},
                                                style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                                style_data_conditional = table_style,
                                                style_header = table_header 
                                                ),
                                                
                                                html.H3('Finals'),
                                                dash_table.DataTable(
                                                # id='datatable-semi-final-predictions',
                                                data=dataTable[2].to_dict('records'),
                                                columns=[{"name": i, "id": i} for i in dataTable[2].columns], 
                                                editable=False,
                                                style_table={'maxWidth': '300px'},
                                                style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                                style_data_conditional = table_style,
                                                style_header = table_header 
                                                ),
                                                
                                                html.H3('Semi Final Teams'),
                                                dash_table.DataTable(
                                                # id='datatable-semi-final-predictions',
                                                data=dataTable[3].to_dict('records'),
                                                columns=[{"name": i, "id": i} for i in dataTable[3].columns], 
                                                editable=False,
                                                style_table={'maxWidth': '300px'},
                                                style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                                style_data_conditional = table_style,
                                                style_header = table_header 
                                                ),
                                                
                                                html.H3('Players'),
                                                dash_table.DataTable(
                                                # id='datatable-semi-final-predictions',
                                                data=dataTable[4].to_dict('records'),
                                                columns=[{"name": i, "id": i} for i in dataTable[4].columns], 
                                                editable=False,
                                                style_table={'maxWidth': '300px'},
                                                style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                                                style_data_conditional = table_style,
                                                style_header = table_header 
                                                ),
                                            ],className = "card-content")
                                        ], className = "card")
                                ], className="col l6"),
                        ], className="row"),
                    ])
                ])
                 
    return showDataLayout


def mainPage():

    rank_data = get_rank_table()

    graph_data = getGraphData()

    optionsDropDown=[{"label": i, "value": j+':'+i} for i,j in zip(rank_data['Name'], rank_data['EMNO'])]

    mainPageLayout = html.Div([

        html.Div([
            html.Div([
                html.H3('World Cup 2019 Predictions')
            ],className = 'card-content')
        ], className = 'card' ),

        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Span(['Rank table'], className = 'card-title'),
                        dash_table.DataTable(
                            data=rank_data.to_dict('records'),
                            columns=[{"name": i, "id": i} for i in rank_data.columns], 
                            editable=False,
                            style_table={'maxWidth': '300px'},
                            style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                            style_data_conditional = [

                                                        {
                                                            'if' : {'row_index': 'odd'},
                                                            'backgroundColor': 'rgb(183,238,255)'
                                                        },

                                                    ],
                            style_header = {'backgroundColor': 'rgb(248,248,248)', 'fontWeight': 'bold'}
                        )
                    ], className = 'card-content')
                ], className = 'card')
            ], className = 'col l4'),

            html.Div([
                html.Div([
                    html.Div([
                        html.Span(['Rank Chart'], className = 'card-title'),
                        dcc.Graph(
                            id='rank-chart',
                            figure = {
                                'data' : [go.Bar(x = rank_data['Name'], y = rank_data['Score'], orientation = 'v')],
                                'layout' :  go.Layout(xaxis={'title' : 'Employees'}, yaxis={'title' : 'Score'})
                            }
                        )
                    ], className = 'card-content')
                ], className = 'card')
            ], className = 'col l8')

        ], className = 'row'),

        html.Div([

            html.Div([
                html.Div([
                    html.Div([
                        html.Span(['Score Progress'], className = 'card-title'),
                        dcc.Graph(
                            id="my-graph",
                            figure = {
                                'data' : graph_data,
                                "layout": go.Layout(colorway=['#fdae61', '#abd9e9', '#2c7bb6'],
                                yaxis={"title": "Points"}, xaxis={"title": "Match"})
                            }
                        )

                    ], className = 'card-content')
                ], className = 'card')
            ], className = 'col l12')

        ], className = 'row'),

        html.Div([

            html.Div([
                html.Div([
                    html.Div([

                        html.Div([
                            html.H3(['Your Predictions']),
                            html.Div([
                                html.Div([
                                    html.Div([
                                        html.Span(['Select your name'], className = 'card-title'),
                                        dcc.Dropdown(
                                            id = 'your-score-dropdown',
                                            options = optionsDropDown
                                        )
                                    ], className = 'card-content')
                                ])
                            ], className = 'col l12')

                        ], className = 'row'),


                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Div(className = 'card-content',id='your-score-container')
                                ])
                            ], className = 'col l12')

                        ], className = 'row')

                    ], className = 'card-content')
                ], className = 'card')
            ], className = 'col l12')

        ], className = 'row')

    ])

    return mainPageLayout