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
from wordcloud import WordCloud          # pip install wordcloud

#bootstrap themes **************************************************************
app = dash.Dash(__name__,use_pages=True, external_stylesheets=[dbc.themes.LUX, dbc.icons.FONT_AWESOME])

#Asset import **************************************************************************

#import App data ************************************************************


#sidebar **********************************************************************************
sidebar = html.Div(
    [
        html.Div([
            html.H2("Welcome", style={"color": "white"}),
        ], className="sidebar-header",),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-house",), html.Span("Dashboard", style={"color": "white"})],
                        href="/",
                        active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-database"), html.Span("Dataset", style={"color": "white"})],
                        href="/dataset",
                        active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-upload"), html.Span("How to upload data", style={"color": "white"})],
                        href="/help",
                        active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-circle-question"), html.Span("About", style={"color": "white"})],
                        href=dash.page_registry['pages.about']['path'],
                        active="exact",
                )
            ],
            vertical=True,
            pills=True,
            class_name="sidebar_height",
        ),
        html.Hr(),
    ],
    className="sidebar",
)


#How to upload

#app.layout**************************************************************
app.layout = html.Div(
    [
        sidebar, 

        
    ]
)

if __name__=='__main__':
    app.run_server(debug=True, port=8021)