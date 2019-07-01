import pandas as pd
import sqlite3
import plotly.graph_objs as go
from get_rank import get_rank_table
from display_individual_data import dispIndvData



def getGraphData():
    rank_table = get_rank_table()
    trace = []
    for (i,j) in zip(rank_table['EMNO'], rank_table['Name']):
        
        indv_data = dispIndvData(i)
        league = indv_data[0]
        league.dropna(inplace=True)
        trace.append(go.Scatter(x=league["Match"], y=league["Points"].cumsum(), name=j, mode='lines',
                marker={'size': 8, "opacity": 0.6, "line": {'width': 0.5}}, ))

    return trace

