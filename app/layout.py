import dash
import dash_core_components as dcc
import dash_html_components as html
import sqlite3
import pandas as pd

conn =  sqlite3.connect("../data_base/predictions.sqlite")
df = pd.read_sql_query("SELECT * FROM predictions", conn)

external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def generate_table(dataframe):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])]  +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(len(dataframe))]
    )
    


app.layout = html.Div(children=[
    html.H1(
        children='IDIADA ICC World Cup 2019 Predictions',
        style={
            'textAlign': 'left',           
        }
    ),

    generate_table(df)

  
])


if __name__ == '__main__':
    app.run_server(debug=True)