import dash_core_components as dcc
import dash_html_components as html
import dash_table

from get_rank import get_rank_table

upload_layout = html.Div(children = [
    html.H3(
        children='Upload Data'
    ), html.P(
        children='Upload the completely filled excel file.(Only *xls/*xlxs files)'
    ),
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
    html.Div(id='output-data-upload'),
])
 

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
                                                    id='datatable-league-predictions',
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
                        data=get_rank_table().to_dict('records'),
                        columns=[{"name": i, "id": i} for i in get_rank_table().columns], 
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
        ], className = 'col l4')
    ], className = 'row')

])