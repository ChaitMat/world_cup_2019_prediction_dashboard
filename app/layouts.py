import dash_core_components as dcc
import dash_html_components as html
import dash_table

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
 

submit_layout =  html.Div([
                    dcc.Location(id='url2', refresh=False),
                    html.Div(id='page-content2')
                        ])

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
    
    showDataLayout = html.Div([
                html.H3('Current score'),
                html.H5('Name: '+ name, id = 'emp-name'),
                html.H5('EM No.: ' + emno, id = 'emp-id'),
                # html.BR(),
                html.H3('Your current score: '+str(score)),
                # html.BR(),
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
