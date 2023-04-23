import dash
from dash import dcc, html
from dash.dependencies import Output, Input
from dash import dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objs as go


import pandas as pd
import data_engine.pick as pick
import data_engine.data_sorter as db 

pick.make_data_df(db.alc_data)
df = pick.data.copy()

fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            html.H1("DATA", className="text-center text-drak mb-4"),
            width=12
        )
    ),
    dbc.Row([
        dbc.Col(dash_table.DataTable(
            df.to_dict('records'), ({'name': i, 'id': i} for i in df.columns)
        )),
    #     dbc.Col(
    #         dcc.Graph(figure=fig)
    #     )
    ])
])
