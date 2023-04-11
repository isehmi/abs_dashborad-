import pandas as pd
from dash import Dash, Input, Output, dcc, html, dash_table

dataflow = pd.read_csv('dataflow.csv')
print(dataflow.loc[0])
tabledsta = dataflow.loc[:, ["dataflowId", "name"]]

# here we get some fonts 
external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

# 
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Analytics: Understand Your Avocados!"

app.layout = html.Div(
    children=[
    # this is a div class for the header 
        html.Div(
            children=[
                html.H1(
                    children="ABS Dashborad", className="header-title"
                ),
                html.P(
                    children=(
                        "Using a API provide by ABS you can find and display data"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
    # this is a div class for the mean 
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="This is WIP but we will have search here", className="menu-title"),
                        dcc.Dropdown(
                            id="dataflowId-filter",
                            value="",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="this is the main body where the table is going", className="table"),
                        dash_table.DataTable(data=tabledsta.to_dict("records"), page_size=10)
                    ]
                )
            ],
            className="menu",
        ),

    ]
)




if __name__ == "__main__":
    app.run_server(debug=True)  