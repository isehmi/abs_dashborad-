import dash
from dash import dcc, html, ctx
from dash.dependencies import Output, Input
from dash import dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import pandas as pd
import data_engine.pick as pick


# ----- formnat dsd table and dropdown -------#
pick.make_dsd_df()
dsd_dropDown_data = 'position ' + pick.dsd['Position'].astype(str)
api_call__ = []



# making the app 
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
app.layout = dbc.Container([
    dbc.Row( 
        dbc.Col(html.H1("Exploring Data Options: Your Guide to Available DSD", #<-- add the name of the dsd you pick from the last page
                        className="text-center text-drak mb-4"), 
                        width=12)
    ),
    dbc.Row([
        dbc.Col([
            html.P("click on the value you want from the table"),
            dcc.Dropdown(
                id='dsd_dropDown',
                multi=False,
                options = dsd_dropDown_data,
                value = dsd_dropDown_data.iloc[0]
            ),
            html.Button('submit', id='submit_button', n_clicks=0),
            html.Div(id='adding_options'),
            html.Button('format API', id='formating_api', n_clicks=0),
            html.Div(id='output_api')
        ]),

        dbc.Col(
            html.Button('clear', id='clear_list', n_clicks=0),
        ),
    ]),
    dbc.Row(
        dbc.Col(
            dash_table.DataTable(
                id='dsd_table'
            )
        )
    )
])

@app.callback(
        Output('adding_options', 'children'),
        Input('submit_button', 'n_clicks'),
        Input('clear_list', 'n_clicks'),
        Input('formating_api', 'n_clicks'),
        State('dsd_table', 'active_cell'),
        State('dsd_dropDown', 'value')
)
def api_opntion(submit_button, clear_button, format_api_button, active_cell, value):
    tiggered_id = ctx.triggered_id
    print(tiggered_id)
    if tiggered_id == 'submit_button':
        return updata_api_opntions(submit_button, active_cell, value)
    elif tiggered_id == 'clear_list':
        return clear_api_opntions()
    elif tiggered_id == 'formating_api':
        return format_api()

# this function gets the actuve cell and adds it to a list if the submit is pressed 
def updata_api_opntions(button, active_cell, value):
    if button > 0:
        positon = value.split(' ') #<- we will also use this when formating api call 
        cell = active_cell['row']
        listthing = pick.dsd["Code"].iloc[int(positon[1])-1][cell]
        print(listthing)
        api_call__.append(listthing)
        # we should add a way to make sure they dont submiint the same value more then once 
    return html.P(api_call__)

# this clears the list is the clear button is pressed 
def clear_api_opntions():
    api_call__.clear()
    return html.P(api_call__)


def format_api():
    base_url = "https://api.data.abs.gov.au/data/ALC/"
    all_options = ''

    for i in api_call__:
        all_options = all_options + str(i) + '.'
    full_api_call = base_url+all_options
    print(full_api_call)
    return html.P(full_api_call)



# this check for what options has been picked for the dropdown 
@app.callback(
    Output('dsd_table', 'data'),
    Input('dsd_dropDown', 'value')
)
def updata_table(value):
    print(value)
    position = value.split(' ')

    dsd_table_data_name = pick.dsd["Name"].iloc[int(position[1])-1].copy()
    dsd_table_data_code = pick.dsd["Code"].iloc[int(position[1])-1].copy()
    dsd_table_data_name.pop(0) # remove that value so it can be used in the table
    dsd_table_data = pd.DataFrame({'name': dsd_table_data_name, 'code':                dsd_table_data_code})

    return dsd_table_data.to_dict('records')


