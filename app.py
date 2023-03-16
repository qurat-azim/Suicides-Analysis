from dash import html, dcc, Input, Output
import dash
import altair as alt
import pandas as pd
from vega_datasets import data
import dash_bootstrap_components as dbc


# Read in global data
cars = data.cars()

df = pd.read_csv("data/master.csv")

# Setup app and layout/frontend
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    html.H1('Suicides Analysis'),
    dbc.Row([
        dbc.Col([
            html.Label("Select Country", htmlFor="xcol-widget"),
            dcc.Dropdown(
                id='xcol-widget',
                value='Brazil',  # REQUIRED to show the plot on the first page load
                options=[{'label': col, 'value': col} for col in df['country'].unique()]),
            html.Label("Select Year", htmlFor="ycol-widget"),
            dcc.Slider(
                id='ycol-widget',
                min=df['year'].unique().min(),
                max=df['year'].unique().max(),
                value=2000,  # REQUIRED to show the plot on the first page load
                marks={1985: '1985', 2020: '2020'})],
            md=4),
        dbc.Col([
            dbc.Row([
                html.H5('Suicides by Gender'),
                html.Iframe(
                    id='bar',
                    style={'border-width': '5', 'width': '100%', 'height': '20vh'})
                ]),
            dbc.Row([
                html.H5('Suicides by Age range'),
                html.Iframe(
                    id='pie',
                    style={'border-width': '5', 'width': '100%', 'height': '80vh'})
                ])
            ])
        ])])
# Set up callbacks/backend
@app.callback(
    Output('bar', 'srcDoc'),
    Input('xcol-widget', 'value'),
    Input('ycol-widget', 'value'))

def plot_altair(xcol, ycol):
    new_df = df[df['year'] == ycol]
    new_df2 = new_df[new_df['country'] == xcol]
   
    chart = alt.Chart(new_df2).mark_bar().encode(
        x=alt.X('suicides_no', title='Number of Suicides'),
        y=alt.Y('sex', title='Gender'),
        color=alt.Color('sex', title='Gender'),
        tooltip=alt.Tooltip(['suicides_no'], title="Suicides")
        ).interactive()
    return chart.to_html()
    

@app.callback(
    Output('pie', 'srcDoc'),
    Input('xcol-widget', 'value'),
    Input('ycol-widget', 'value'))

def plot_pie_altair(xcol, ycol):
    new_df = df[df['year'] == ycol]
    new_df2 = new_df[new_df['country'] == xcol]

    chart = alt.Chart(new_df2).mark_arc().encode(
        theta=alt.Theta(field="suicides_no", type="quantitative"),
        color=alt.Color(field="age", type="nominal", title="Age"),
        tooltip=alt.Tooltip(['suicides_no'], title="Suicides")
    )
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)