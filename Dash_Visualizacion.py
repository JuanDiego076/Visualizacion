from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('C:/Users/juand/OneDrive/Escritorio/global-data-on-sustainable-energy.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Dashboard con 5 Gráficos', style={'textAlign':'center'}),

    # Agrega el componente Dropdown
    dcc.Dropdown(options=[{'label': Entity, 'value': Entity} for Entity in df['Entity'].unique()], value='Colombia', id='dropdown-selection'),
    # Gráfico de barras
    dcc.Graph(id='graph-bar'),
    # Gráfico de dispersión
    dcc.Graph(id='graph-scatter'),
    # Gráfico de líneas
    dcc.Graph(id='graph-line'),
    # Gráfico de tarta
    dcc.Graph(id='graph-pie'),
    # Gráfico de área
    dcc.Graph(id='graph-area')
])

@callback(
    Output('graph-bar', 'figure'),
    Output('graph-scatter', 'figure'),
    Output('graph-line', 'figure'),
    Output('graph-pie', 'figure'),
    Output('graph-area', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.Entity==value]
    # Gráfico de barras
    bar_fig = px.bar(dff, x='Year', y='Access to electricity (% of population)', title='Gráfico de Barras')
    # Gráfico de dispersión
    scatter_fig = px.scatter(dff, x='Year', y='Renewable-electricity-generating-capacity-per-capita', title='Gráfico de Dispersión')
    # Gráfico de líneas
    line_fig = px.line(dff, x='Year', y='Access to electricity (% of population)', title='Gráfico de Líneas')
    # Gráfico de tarta
    pie_fig = px.pie(dff, names='Primary energy consumption per capita (kWh/person)', title='Gráfico de Tarta')
    # Gráfico de área
    area_fig = px.area(dff, x='Year', y='Access to electricity (% of population)', title='Gráfico de Área')

    return bar_fig, scatter_fig, line_fig, pie_fig, area_fig

if __name__ == '__main__':
    app.run(debug=True)