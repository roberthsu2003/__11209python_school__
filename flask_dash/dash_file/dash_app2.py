from dash import Dash, html
import pandas as pd
import dash_bootstrap_components as dbc

dash2 = Dash(requests_pathname_prefix="/dash/app2/",external_stylesheets=[dbc.themes.BOOTSTRAP])

dash2.layout = html.Div(
    [html.H1("BootStrap Layout"),
     html.P("這是段落1"),
     html.P("這是段落2")
    ],
    className="container-lg",
    style={'backgroundColor':'#666'}

    )
