from dash import Dash, html, dash_table, dcc,callback, Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app2 = Dash(requests_pathname_prefix="/app2/",external_stylesheets=external_stylesheets)
app2.layout = html.Div([
    html.Div(
        className="row",
        children="我的第一個App和圖表顯示,並使用控制項",
        style={'textAlign':'center','color':'blue','fontSize':30}
    ),
    html.Div(className='row',children=[
        dcc.RadioItems(
            options=['pop', 'lifeExp', 'gdpPercap'],
            value='lifeExp',
            id='my-radio-buttons-final')
    ]),
    html.Div(className='row',children=[
        html.Div(
            className='six columns',children=[
                dash_table.DataTable(
                data=df.to_dict('records'),
                page_size=10,
                style_table={'overflowX': 'auto'})
            ]
        ),
        html.Div(
            className='six columns',children=[
            dcc.Graph(figure={},id='histo-chart-final')
        ])
    ]),
    
])

@callback(
    Output(component_id='histo-chart-final', component_property='figure'),
    Input(component_id='my-radio-buttons-final', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig


