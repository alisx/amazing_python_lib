import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np

app = dash.Dash(__name__)

# 设定应用的布局
app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Option 1', 'value': '1'},
            {'label': 'Option 2', 'value': '2'},
            {'label': 'Option 3', 'value': '3'}
        ],
        value='1'
    ),
    dcc.Graph(id='graph')
])

# 设定回调函数
@app.callback(
    Output('graph', 'figure'),
    Input('dropdown', 'value')
)
def update_graph(value):
    # 生成随机数据
    np.random.seed(int(value))  # 用选项值作为随机数种子，以便每个选项都有固定的数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.randn(100) * 0.2

    # 创建图表
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)