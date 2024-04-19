import dash                              # pip install dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
from datetime import date

from dash_extensions import Lottie       # pip install dash-extensions
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px              # pip install plotly
import pandas as pd                      # pip install pandas
from datetime import date
import calendar
from wordcloud import WordCloud  

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, dbc.icons.FONT_AWESOME])


layout = html.Div([
    html.Div([
        html.H2("How to Download and upload your LinkedIn data."),
        html.P(["The easiest and fastest way to obtain a copy of your LinkedIn data is to initiate a data download from your ", html.A("Settings & Privacy page:", href="https://www.linkedin.com/psettings/data-privacy/", target="_blank")]),
        html.Hr(),
    ]),
    html.Div( className='div_two', children=[
        html.Div([
            html.Div(className='icon-text', children=[
                html.I(className="fa-solid fa-1"),
                html.P(["Click the ", html.Span("Me", style={'fontWeight': '700'}), " icon at the top of your LinkedIn homepage."]),
            ]),
            html.Div(className='icon-text', children=[
                html.I(className="fa-solid fa-2"),
                html.P(["Select", html.Span(" Settings & Privacy ", style={'fontWeight': '700'}), "from the dropdown."]),
            ]),
            html.Div(className='icon-text', children=[
                html.I(className="fa-solid fa-3"),
                html.P(["Click the", html.Span(" Data Privacy ", style={'fontWeight': '700'}), "on the left rail."]),
            ]),
            html.Div(className='icon-text', children=[
                html.I(className="fa-solid fa-4"),
                html.P(["Under the", html.Span(" How LinkedIn uses your data ", style={'fontWeight': '700'}), "section, click", html.Span(" Get a copy of your data. ", style={'fontWeight': '700'})]),
            ]),
            html.Div(className='icon-text', children=[
                html.I(className="fa-solid fa-5"),
                html.P(["Select the data that you’re looking for and", html.Span(" Request archive. ", style={'fontWeight': '700'})]),
            ]),
        ],)
    ], style={'textAlign' : 'center'}),
    html.Div([
        html.Hr(),
        html.P("Then Go to dashboard section and click upload data and upload the respective files."),
    ]),
], style={'textAlign' : 'center'})

