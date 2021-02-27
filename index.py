from app import app
from app import server

from utils import Data
from components import Table, BarPlot, BoxPlot

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from datetime import datetime

## Data Loading
data = Data() 
prepared_data = data.retrieve_prepared_data()
splitted_data = data.retrieve_splitted_date_data()
peak_values_and_dates = data.retrieve_peak_values_and_dates()
slope_changes_and_dates = data.retrieve_slope_changes_and_dates()

# Importing components
table = Table()
barplot = BarPlot()
boxplot = BoxPlot()

## App Layout
app.layout = html.Div([html.H1('Data Report',
                               style = {
                                      'textAlign': 'center',
                                      'background': '7f44f8',
                                      'color': 'white'}),
             html.Div(['Date selector for the interactive graphic',
                       dcc.DatePickerRange(
                        id = 'date-input',
                        stay_open_on_select = False,
                        min_date_allowed = datetime(2021, 1, 24, 0, 0),
                        max_date_allowed = datetime(2021, 1, 27),
                        initial_visible_month = datetime(2021, 1, 1),
                        start_date = datetime(2021, 1, 24),
                        end_date = datetime(2021, 1, 27),
                        number_of_months_shown = 1,
                        month_format = 'MMMM,YYYY',
                        display_format = 'YYYY-MM-DD',
                        style = {
                               'color': '#7f44f8',
                               'font-size': '18px'
                        }
            ),
            html.Div(id='date-output')
                ], className = "row ",
                   style = {'marginTop': 0, 'marginBottom': 0, 'font-size': 25, 'color': 'white'}),
            html.Div(id='graph-output'),
                dcc.Graph(
                         id = 'peaks_table',
                         figure = table.create(peak_values_and_dates, 'Date', 'Values', 'Dates at where there are peaks')
                        ),
            html.Div(id = 'peaks_table_div'),
                dcc.Graph(
                         id = 'slope_changes_table',
                         figure = table.create(slope_changes_and_dates, 'Date', 'Slope changes to', 'Dates at where there are slope changes')
                        ),
            html.Div(id = 'slope_changes_table_div'),
                dcc.Graph(
                         id = 'day_barplot',
                         figure = barplot.create(splitted_data, 'day', 'Values', 'Values group by day')
                        ),
            html.Div(id = 'days_barplot'),
                dcc.Graph(
                         id = 'hour_barplot',
                         figure = barplot.create(splitted_data, 'hour', 'Values', 'Values group by hour')
                        ),
            html.Div(id = 'hours_barplot'),
                dcc.Graph(
                         id = 'day_boxplot',
                         figure = boxplot.create(splitted_data, 'day', 'Values', 'Values group by hour')
                        ),
            html.Div(id = 'days_boxplot'),
                dcc.Graph(
                         id = 'hour_boxplot',
                         figure = boxplot.create(splitted_data, 'hour', 'Values', 'Values group by hour')
                        ),
            html.Div(id = 'hours_boxplot'),
            html.Div([
                        html.H1('Insights', style = {'fontSize': 40}),
                        html.P('From the exploratory data analysis, i saw that the data is from a time series, ' + 
                               'and the timestamps columns was string data type. Also in this column, there was a NaN ' +
                               'and a bad string. This may be due to a ' +
                               'lack of validation in the data entry, or a typo. ' + 
                               'When i graphed the data, i saw some peak and changes in the slopes. ' + 
                               'Because i dont have any backround of this data, i dont know if this peaks ' +
                               'are possibles or if they are outliers, ' +
                               'because this values significantly differ from the patterns and trends of the other values ' + 
                               'in the time series. ' +
                               'From the boxplot graphics, i saw that the Jan 25 has the biggest range ' + 
                               'of values and the biggest median. Between the 14 and 21 hours, the interquartile range is the biggest. ' + 
                               'The bar plot graphics provides similar information information (values per day and hour).',
                               className = 'my-class', id = 'insights', style = {'fontSize': 15, 'text-align': 'left'})
                    ], style = {'background': 'white'})
                ], style = {"background": "#7f44f8"},
            )

## App callback
@app.callback(Output('graph-output', 'children'),
              [Input('date-input', 'start_date'),
               Input('date-input', 'end_date')])
def render_interactive_graph(start_date, end_date):
    data = prepared_data[(prepared_data.Timestamps >= start_date) & (prepared_data.Timestamps <= end_date)]
    return dcc.Graph(
        id = 'graph-1',
        figure = {
            'data': [
                {'x': data['Timestamps'], 'y': data['Values'], 'type': 'line', 'name': 'value1', 'marker' : { "color" : '#7f44f8'}},
            ],
            'layout': {
                'title': 'Values vs Timestamps interactive graphic',
                'plot_bgcolor': 'white',
                'paper_bgcolor': 'white',
                'font': {
                    'color': '#7f44f8',
                    'size': 18
                },
                'xaxis': {
                        'title': 'Timestamps',
                        'showspikes': True,
                        'spikedash': 'dot',
                        'spikemode': 'across',
                        'spikesnap': 'cursor',
                        },
                'yaxis': {
                        'title': 'Values',
                        'showspikes': True,
                        'spikedash': 'dot',
                        'spikemode': 'across',
                        'spikesnap': 'cursor'
                        },

            }
        }
    )


if __name__ == '__main__':
    app.run_server(debug=True)
