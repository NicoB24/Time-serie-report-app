import plotly.graph_objects as go
import plotly.express as px
import dash_core_components as dcc

class Table():    
    def create(self, values, first_column_name, second_column_name, titles):
        return go.Figure(data = [go.Table(
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

class BarPlot():
    def create(self, data, x, y, titles):
        return go.Figure(data = [go.Bar(
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

class BoxPlot():
    def create(self, data, x, y, titles):
        return px.box(data, x = x, y = y, title = titles)
