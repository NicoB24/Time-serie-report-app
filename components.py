import plotly.graph_objects as go
import plotly.express as px
import dash_core_components as dcc

class DatePickerRange():
    def render(self, min_date_allowed, max_date_allowed, initial_visible_month, start_date, end_date, number_of_months_shown, id_name):
        return dcc.DatePickerRange(
            id = id_name,
            stay_open_on_select = False,
            min_date_allowed = min_date_allowed,
            max_date_allowed = max_date_allowed,
            initial_visible_month = initial_visible_month,
            start_date = start_date,
            end_date = end_date,
            number_of_months_shown = number_of_months_shown,
            month_format = 'MMMM,YYYY',
            display_format = 'YYYY-MM-DD',
            style = {
                        'color': '#7f44f8',
                        'font-size': '18px'
                    }
        )

class Table():    
    def render(self, values, first_column_name, second_column_name, titles, id_name):
        return dcc.Graph(
            id = id_name,
            figure = go.Figure(data = [go.Table(
                               columnorder = [1,2],
                               columnwidth = [50,50],
                               header = dict(
                                    values = [[first_column_name],
                                             [second_column_name]],
                                    line_color = 'darkslategray',
                                    fill_color = '#7f44f8',
                                    align = ['left','center'],
                                    font = dict(color = 'white', size = 12),
                                    height = 40
                                    ),
                               cells = dict(
                                    values = values,
                                    line_color = 'darkslategray',
                                    fill = dict(color=['#39c2b6', 'white']),
                                align = ['left', 'center'],
                                font_size = 12,
                                height = 30)
                                    )
                                ],
                                layout = go.Layout(
                                        title = go.layout.Title(text = titles)
                                )
                            )
                        )

class BarPlot():
    def render(self, data, x, y, titles, id_name):
        return dcc.Graph(
            id = id_name,
            figure = go.Figure(data = [go.Bar(
                                        x = data[x], y = data[y],
                                        textposition = 'auto'
                                      )],
                                layout = go.Layout(
                                title = go.layout.Title(text = titles),
                                height = 800,
                                xaxis_title = x,
                                yaxis_title = y,
                               )
                            )
         )

class BoxPlot():
    def render(self, data, x, y, titles, id_name):
        return dcc.Graph(
            id = id_name,
            figure = px.box(data, x = x, y = y, title = titles)
        )


class InteractivePlot():
    def render(self, data, x, y, title, id_name):
        return dcc.Graph(
            id = id_name,
            figure = {
                'data': [
                    {'x': data[x], 'y': data[y], 'type': 'line', 'name': 'value1', 'marker' : { "color" : '#7f44f8'}},
                ],
                'layout': {
                    'title': title,
                    'plot_bgcolor': 'white',
                    'paper_bgcolor': 'white',
                    'font': {
                        'color': '#7f44f8',
                        'size': 18
                    },
                    'xaxis': {
                            'title': x,
                            'showspikes': True,
                            'spikedash': 'dot',
                            'spikemode': 'across',
                            'spikesnap': 'cursor',
                            },
                    'yaxis': {
                            'title': y,
                            'showspikes': True,
                            'spikedash': 'dot',
                            'spikemode': 'across',
                            'spikesnap': 'cursor'
                            },

                }
            }
        )
