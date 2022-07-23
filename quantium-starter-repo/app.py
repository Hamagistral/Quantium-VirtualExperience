
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


app = Dash(__name__)

app.title = "Soul Foods Data Viz"

df = pd.read_csv('./data/processedDF2')

fig = px.line(df, x="date", y="sales")

app.layout = html.Div(style={'padding': 10}, children=[
    html.H1(
        children='Pink Morsel Sales Visualization',
        style={
            'textAlign': 'center',
            'font-family':'sans-serif'
        }
    ),
    
    html.Div([
      html.Label('Choose the region : '),
      html.Br(),
      dcc.RadioItems([{'label': 'Noth', 'value': 'north'}, {'label': 'South', 'value': 'south'},
      {'label': 'East', 'value': 'east'}, {'label': 'West', 'value': 'west'}], 'north', id='region', inline=True),
    ], style={'display': 'flex', 'textAlign': 'center', 'font-family':'sans-serif', 'alignItems': 'center', 'justifyContent': 'center', 'margin': '10px'}),

    dcc.Graph( 
        id='salesGraph',
        figure=fig,
    )
])

@app.callback(
    Output('salesGraph', 'figure'),
    Input('region', 'value'))

def update_graph(region):
    dff = df[df['region'] == region]

    fig = px.line(dff, x="date", y="sales", template = "ggplot2")

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
