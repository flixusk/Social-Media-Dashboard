import dash                              # pip install dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
from datetime import date
import base64
import datetime
import io


from dash_extensions import Lottie       # pip install dash-extensions
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px              # pip install plotly
import pandas as pd                      # pip install pandas
from datetime import date
import calendar
from wordcloud import WordCloud          # pip install wordcloud


#bootstrap themes **************************************************************
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, dbc.icons.FONT_AWESOME])

#Asset import **************************************************************************
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))
url_conections = "https://lottie.host/2774465d-b091-4c2f-92bf-dd648431ab07/N7afCDBtnG.json"
url_company ="https://lottie.host/31fa89ac-9103-4cb1-b796-8668c13a5c2e/Je59syniVm.json"
url_inv_in = "https://lottie.host/6c015896-8132-4301-8f5d-cbf2f8b4342d/GNA8ttj40d.json"
url_inv_out = "https://lottie.host/b263d68c-8f8a-412b-8600-283923713071/1NkbbHVFaB.json"
url_reaction = "https://lottie.host/0c2e48ac-fdc7-49db-a1a7-dbfe4e0b74c7/VsMTkCvRV3.json"

connection_image = '/static/images/social-media.gif'
#import App data ************************************************************






#Cards *********************************************************
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Dashboard")
        ],style={'textAlign' : 'left', 'padding' : '15px'} ),
        dbc.Col([
            dcc.Upload(
                html.Button('Upload Files'),
                style={
                
                },
                multiple=True,
                ),

        ],style={'padding' : '15px', 'textAlign' : 'center'})
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


#upload


def parse_content(content, filename, date):
    content.type, content_string = content_string(',')

    decode = base64.b64decode(content_string)

    try:
        if 'csv' in filename:
            #if the file is csv
            df = pd.read_csv(
                io.StringIO(decode.decode('utf-8'))
            )
        elif 'xls' in filename:
            #if the file is xls
            df = pd.read_excel(io.BytesIO(decode))
    except Exception as e:
        print(e)
        return html.Div([
            'there was a an error processing this file'
        ])
