from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
dash2 = Dash(requests_pathname_prefix="/dash/app2/")

dash2.layout = html.Div([
    html.H1(children='Dash Layout 開始了', style={'textAlign':'center'})

])