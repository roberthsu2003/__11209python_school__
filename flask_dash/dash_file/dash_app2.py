from dash import Dash, html,dash_table
import pandas as pd
import dash_bootstrap_components as dbc

dash2 = Dash(requests_pathname_prefix="/dash/app2/",external_stylesheets=[dbc.themes.BOOTSTRAP])
dash2.title = "台北市youbike及時資料"

df = pd.DataFrame({
    "水果": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "數量": [4, 1, 2, 2, 4, 5],
    "城市": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

dash2.layout = html.Div(
    [
        dbc.Container([
            html.Div([
                html.Div([
                    html.H1("台北市youbike及時資料")
                ],className="col text-center")
            ],
            className="row",
            style={"paddingTop":'2rem'}),
            html.Div([
                html.Div([
                    dash_table.DataTable(df.to_dict('records')),
                ],className="col text-center")
            ],
            className="row",
            style={"paddingTop":'2rem'}),
        ])
    ],
    className="container-lg"
    )
