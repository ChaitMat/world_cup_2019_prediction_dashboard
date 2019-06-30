import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from layouts import upload_layout, mainPage
import callbacks
from callbacks import submit

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
            submit_layout = submit(pathname)
            return submit_layout 
        elif pathname == '/':
            main_page_layout = mainPage()
            return main_page_layout
        else:
            return '404'

    else:
         return '404'

if __name__ == '__main__':
    app.run_server(debug=True)