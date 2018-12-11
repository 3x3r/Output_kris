import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_excel('C:\\Python27/upload.xlsx','Лист1')
pv = pd.pivot_table(df, index=['forsage'],values=["tSolidLine","nOverSpeed","nRedLight","nWrongDirection","tRoadSide","tStopLine","tOneDirection"])
#available_indicators = df['forsage'].unique()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


trace1 = go.Bar(x=pv.index, y=pv[('tSolidLine')], name='tSolidLine')
trace2 = go.Bar(x=pv.index, y=pv[('nOverSpeed')], name='nOverSpeed')
trace3 = go.Bar(x=pv.index, y=pv[('nRedLight')], name='nRedLight')
trace4 = go.Bar(x=pv.index, y=pv[('nWrongDirection')], name='nWrongDirection')
trace5 = go.Bar(x=pv.index, y=pv[('tRoadSide')], name='tRoadSide')
trace6 = go.Bar(x=pv.index, y=pv[('tStopLine')], name='tStopLine')
trace7 = go.Bar(x=pv.index, y=pv[('tOneDirection')], name='tOneDirection')
app.layout = html.Div(children=[
    html.H1(children='Forsage Report'),
    html.Div(children='''Violations Forsage Report.'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1,trace2,trace3,trace4,trace5,trace6,trace7],
            'layout':
            go.Layout(title='Таблица', barmode='stack')
        })
])
if __name__ == '__main__':
    app.run_server(debug=True)