import dash_core_components as dcc
import dash_html_components as html

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
 

submit_layout = html.Div(html.H3()) 

