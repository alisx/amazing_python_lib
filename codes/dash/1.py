# 布局示例
from dash import Dash, html, dcc
app = Dash(__name__)
app.layout = html.Div([
    dcc.Graph(id='example-graph'),
    dcc.Dropdown(id='example-dropdown'),
    html.Button('Click me', id='example-button')
])
app.run()