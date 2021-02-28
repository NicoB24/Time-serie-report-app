from app import app
from app import server

from utils import Data
from constants import peak_values_and_dates, slope_changes_and_dates, insights
from components import DatePickerRange, Table, BarPlot, BoxPlot, InteractivePlot

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime

## Data Loading
data = Data() 
prepared_data = data.retrieve_prepared_data()
splitted_data = data.retrieve_splitted_date_data()

# Importing components
date_picker_range = DatePickerRange()
table = Table()
bar_plot = BarPlot()
box_plot = BoxPlot()
interactive_plot = InteractivePlot()


## App Layout
app.layout = html.Div([html.H1('Data Report',
                               style = {
                                      'textAlign': 'center',
                                      'background': '7f44f8',
                                      'color': 'white'}),
             html.Div(['Date selector for the interactive graphic',
                       date_picker_range.render(datetime(2021, 1, 24), datetime(2021, 1, 27), datetime(2021, 1, 1), datetime(2021, 1, 24),
                                                datetime(2021, 1, 27), 1, 'date-input'),
             html.Div(id = 'date-output')
                 ], className = "row ",
                    style = {'marginTop': 0, 'marginBottom': 0, 'font-size': 25, 'color': 'white'}),
             html.Div(id = 'graph-output'),
                 table.render(peak_values_and_dates, 'Date', 'Values', 'Dates at where there are peaks', 'peaks_table'),
             html.Div(id = 'peaks_table_div'),
                 table.render(slope_changes_and_dates, 'Date', 'Slope changes to', 'Dates at where there are slope changes', 'slope_changes_table'),
             html.Div(id = 'slope_changes_table_div'),
                 bar_plot.render(splitted_data, 'day', 'Values', 'Values group by day', 'day_barplot'),
             html.Div(id = 'days_barplot'),
                 bar_plot.render(splitted_data, 'hour', 'Values', 'Values group by hour', 'hour_barplot'),
             html.Div(id = 'hours_barplot'),
                 box_plot.render(splitted_data, 'day', 'Values', 'Values group by hour', 'day_boxplot'),
             html.Div(id = 'days_boxplot'),
                 box_plot.render(splitted_data, 'hour', 'Values', 'Values group by hour', 'hour_boxplot'),
             html.Div(id = 'hours_boxplot'),
             html.Div([
                         html.H1('Insights', style = {'fontSize': 40}),
                         html.P(insights, className = 'my-class', id = 'insights', style = {'fontSize': 15, 'text-align': 'left'})
                     ], style = {'background': 'white'})
                 ], style = {"background": "#7f44f8"},
             )

## App callback
@app.callback(Output('graph-output', 'children'),
              [Input('date-input', 'start_date'),
               Input('date-input', 'end_date')])
def render_interactive_graph(start_date, end_date):
    data = prepared_data[(prepared_data.Timestamps >= start_date) & (prepared_data.Timestamps <= end_date)]
    return interactive_plot.render(data, 'Timestamps', 'Values', 'Values vs Timestamps interactive graphic', 'interactive-graph')


if __name__ == '__main__':
    app.run_server(debug=True)
