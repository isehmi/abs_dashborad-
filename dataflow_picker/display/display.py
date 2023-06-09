import dash
from dash import dcc, html
from dash.dependencies import Output, Input
from dash import dash_table
import plotly.express as px
import dash_bootstrap_components as dbc

import pandas as pd
import data_engine.pick as pick

# need to add some functions to work with the pandas files that come from pick
pick.make_dataFlow_df()
dataFlow_search = pick.dataFlow[["name", "dataflowId"]].dropna()
print(dataFlow_search)

dataFlow_table_data = pick.dataFlow[['dataflowId','name', 'description']]
print(dataFlow_table_data)

# ------------------------

# ill add test df here these will all need to be removed 
from plotly.express import data

df =  data.medals_long()

# ------------------------

# BOOTSTRAP, if i want dark mode use DARKLY but this is wip
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
# to do list 
    # i need to change the themes 



app.layout = dbc.Container([
    dbc.Row( # this is for the heading 
        dbc.Col(html.H1("ABS api dashboard", 
                        className="text-center text-drak mb-4"), 
                        width=12)
    ),

    dbc.Row( # this is for seclecing dsd 
        dbc.Col(
            dcc.Dropdown(id='dataFlow_search_dropdown',
                         multi=False,
                         optionHeight=50,
                         searchable=True,
                         placeholder="you can use the full name or data flow ID to search",
                         options=[{'label': name, 'value': dataflowId}
                                  for name, dataflowId in dataFlow_search[["name", "dataflowId"]].to_records(index=False)],
                                    value=dataFlow_search["dataflowId"].iloc[0]
                            ),
                    )
    ),
    dbc.Row([ # this will be the table
        dbc.Col(
            dash_table.DataTable(
                data=dataFlow_table_data.to_dict('records'),
                columns=[{'id':c, 'name': c}for c in dataFlow_table_data.columns],
                page_action='none',
                style_table={'height': '800px', 'width': '100%',  'overflowY': 'auto', 'overflow-wrap': 'break-word'},
                style_cell={'textAlign': 'left', 'max-height': '30px', 'min-height': '30px', 'height': '30px', 'max-width': '150px'},
                style_header={'backgroundColor': 'rgb(30, 30, 30)',
                               'color': 'white'},
                style_data={'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white'},
                css=[{
                    'selector': '.dash-table-tooltip',
                    'rule': 'background-color: black;'
                     }],
                style_cell_conditional=[
                    {'if': {'column_id':'dataflowId'},
                     'width': '15%'}
                ],
                tooltip_data=[
                    {
                        column: {'value': str(value), 'type': 'markdown'}
                        for column, value in row.items()
                    } for row in dataFlow_table_data.to_dict('records')
                ],
                tooltip_duration=None
            )
        )
    ])
])

@app.callback(
    Output('dataFlow_search_dropdown', 'value'),
    Input('dataFlow_search_dropdown', 'value')
)
def submit_dropdown(value):
    print("------Submint----------\n"+ value)