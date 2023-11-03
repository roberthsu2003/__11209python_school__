from dash import Dash, html, dash_table, dcc

app2 = Dash(requests_pathname_prefix="/app2/")
app2.layout = html.Div("Hello, Dash app 2!")