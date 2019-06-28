import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from layouts import upload_layout, submit_layout
import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname != None:
        if pathname == '/upload_file':
            return upload_layout
        elif pathname.startswith('/submit/'):
            return submit_layout 
        else:
            return '404'

    else:
         return '404'

if __name__ == '__main__':
    app.run_server(debug=True)