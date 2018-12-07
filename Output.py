# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
df = pd.read_excel('C:\\Python27/upload.xlsx','Лист1', index_col=None, na_values=['NA'])
#pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
#wb = openpyxl.load_workbook(filename='C:\\Python27/upload.xlsx')
#sheet = wb['Лист1']
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
           {'label': 'F401', 'value': 'F401'},
           {'label': 'F402', 'value': 'F402'},
           {'label': 'F403', 'value': 'F403'},
           {'label': 'F404', 'value': 'F404'},
           {'label': 'F405', 'value': 'F405'},
           {'label': 'F406', 'value': 'F406'},
           {'label': 'F407', 'value': 'F407'},
           {'label': 'F408', 'value': 'F408'},
           {'label': 'F409', 'value': 'F409'},
           {'label': 'F413', 'value': 'F413'},
        ],
        value=['F401', 'F402'],
        multi=True
    ),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': '444'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])
#wb.save('C:\\Python27/upload.xlsx')
if __name__ == '__main__':
    app.run_server(debug=True)
