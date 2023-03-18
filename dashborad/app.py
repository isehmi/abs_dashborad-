import pandas as pd
from dash import Dash, Input, Output, dcc, html

# this is for the project 
flowpicker = (pd.read_csv("test_set.csv"))

# print(flowpicker["dataflowId"].head() )

dataflowId = flowpicker["dataflowId"].head()



# this is from the tut


# here i need to open a csv file(or link to my other python files) to get data 
data = (
    pd.read_csv("avocado.csv")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)
# regions = data["region"].sort_values().unique()

regions = dataflowId 

avocado_types = data["type"].sort_values().unique()


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
                        html.Div(children="DataflowId", className="menu-title"),
                        dcc.Dropdown(
                            id="dataflowId-filter",
                            options=[
                                {"label": Id, "value": Id}
                                for Id in regions
                            ],
                            value="ABORIGINAL_POP_PROJ",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),

            ],
            className="menu",
        ),
    ]
)


@app.callback(
    Output("price-chart", "figure"),
    Output("volume-chart", "figure"),
    Input("region-filter", "value"), # TODO needs changing 
    Input("type-filter", "value"),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
)
def update_charts(region, avocado_type, start_date, end_date):
    filtered_data = data.query(
        "region == @region and type == @avocado_type"
        " and Date >= @start_date and Date <= @end_date"
    )
    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Average Price of Avocados",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "$", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    volume_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Total Volume"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": "Avocados Sold", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return price_chart_figure, volume_chart_figure


if __name__ == "__main__":
    app.run_server(debug=True)  