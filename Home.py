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
from pages import about, how_to, home

#bootstrap themes **************************************************************
app = dash.Dash(__name__,use_pages=True, external_stylesheets=[dbc.themes.LUX, dbc.icons.FONT_AWESOME])

#Asset import **************************************************************************
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))
url_conections = "https://lottie.host/2774465d-b091-4c2f-92bf-dd648431ab07/N7afCDBtnG.json"
url_company ="https://lottie.host/31fa89ac-9103-4cb1-b796-8668c13a5c2e/Je59syniVm.json"
url_inv_in = "https://lottie.host/6c015896-8132-4301-8f5d-cbf2f8b4342d/GNA8ttj40d.json"
url_inv_out = "https://lottie.host/b263d68c-8f8a-412b-8600-283923713071/1NkbbHVFaB.json"
url_reaction = "https://lottie.host/0c2e48ac-fdc7-49db-a1a7-dbfe4e0b74c7/VsMTkCvRV3.json"

connection_image = '/static/images/social-media.gif'
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
                        href="/about",
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






#Cards *********************************************************
dashboard = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Dashboard")
        ],style={'textAlign' : 'left', 'padding' : '15px'} )
    ],className='mb-5'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="60px", height="40px", url=url_conections)),
                dbc.CardBody([
                    html.H6('Connections'),
                    html.H2(id='connection_id', children='000')
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="60px", height="40px", url=url_company)),
                dbc.CardBody([
                    html.H6('COMPANIES'),
                    html.H2(id='company_id', children='000')
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="60px", height="40px", url=url_inv_in)),
                dbc.CardBody([
                    html.H6('INVITES REVEIVED'),
                    html.H2(id='invitesR_id', children='000')
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="60px", height="40px", url=url_inv_out)),
                dbc.CardBody([
                    html.H6('INVITES SENT'),
                    html.H2(id='invitesSend', children='000')
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="60px", height="40px", url=url_reaction)),
                dbc.CardBody([
                    html.H6('REACTION'),
                    html.H2(id='Rreaction', children='000')
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
    ],className='mb-4'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='bar-chart', figure={}),
                ])
            ])
        ],width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='pie-chart', figure={}),
                ])
            ])
        ],width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='Worldcloud', figure={}),
                ])
            ])
        ],width=3)
    ],className='mb-4'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="line-chart", figure={}),
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="idk-for-now", figure={}),
                ])
            ])
        ], width=4)
    ], class_name='mb-3'),
], fluid=True)

#How to upload

#app.layout**************************************************************
app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        sidebar,
        html.Div(
            [
                html.Div(id='page-content')
            ],
            className="content",
        ),
        
    ]
)

# Callback to update page content based on URL
@app.callback(Output('page-content', 'children'),
[Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/about':
        return about.layout
    elif pathname == '/help':
        return how_to.layout
    elif pathname == '/':
        return home.layout
    else:
        return html.Div([
            html.H3('Page not found'),
            html.P('The requested page was not found.')
        ])

if __name__=='__main__':
    app.run_server(debug=True, port=8021)