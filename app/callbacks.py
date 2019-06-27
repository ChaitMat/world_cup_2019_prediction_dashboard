import base64

from dash.dependencies import Input, Output, State

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
                getIndvData(decoded)

        except Exception as e:
            print(e)