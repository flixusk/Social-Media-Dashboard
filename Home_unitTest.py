import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from datetime import datetime as dt
import plotly.express as px
from datetime import date

app = dash.Dash(__name__)

# Sample data
data = px.data.stocks()
fig = px.line(data, x='date', y='GOOG')

app.layout = html.Div([
    dcc.Input(
        id='date-picker',
        type=date,
        value=dt(2024, 3, 1).strftime('%Y-%m-%d'),
        style={'display': 'none'}  # Hide the default input field
    ),
    html.Script(
        """
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('date-picker').click(); // Click on the hidden input field to open the calendar
        });
        """
    ),
    dcc.Graph(
        id='graph',
        figure=fig
    )
])
if __name__ == '__main__':
    app.run_server(debug=True, port=8002)