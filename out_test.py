import time
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime as dt

df = pd.read_excel('C:\\Python27/upload.xlsx','Лист1',index_col=[0])
df.index = pd.to_datetime(df.index, format='%d-%m-%Y %H:%M:%S' )
pv = pd.pivot_table(df, index=['forsage'],values=["tSolidLine","nOverSpeed","nRedLight","nWrongDirection","tRoadSide","tStopLine","tOneDirection"], aggfunc='sum')
#available_indicators = df['forsage'].unique()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

trace1 = go.Bar(x=pv.index, y=pv[('tSolidLine')], name='tSolidLine')
trace2 = go.Bar(x=pv.index, y=pv[('nOverSpeed')], name='nOverSpeed')
trace3 = go.Bar(x=pv.index, y=pv[('nRedLight')], name='nRedLight')
trace4 = go.Bar(x=pv.index, y=pv[('nWrongDirection')], name='nWrongDirection')
trace5 = go.Bar(x=pv.index, y=pv[('tRoadSide')], name='tRoadSide')
trace6 = go.Bar(x=pv.index, y=pv[('tStopLine')], name='tStopLine')
trace7 = go.Bar(x=pv.index, y=pv[('tOneDirection')], name='tOneDirection')
for i in df.index.unique():
    print ('Label {}'.format(str(i)))
    print(time.strptime(str(i),'%Y-%m-%d %H:%M:%S').tm_year)
print('index',df.index)
print ('unique',df.index.unique())
print ('MAX',df.index.max())
app.layout = html.Div(children=[
generate_table(df),
    dcc.Slider(
        min=0,
        max=10,
        marks={
            0: '0 °F',
            3: '3 °F',
            5: '5 °F',
            7.65: '7.65 °F',
            10: '10 °F'
        },
        value=5
    ),
    dcc.DatePickerRange(
        end_date=dt.now(),
        display_format='MMM Do, YY',
        start_date_placeholder_text='MMM Do, YY'
    )
    ,
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