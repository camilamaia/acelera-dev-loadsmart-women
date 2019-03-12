from plotly import tools, plotly, graph_objs


def plot_pie(labels, values):
    # authenticate with your credentials:
    # tools.set_credentials_file(username='', api_key='')

    print('\nLoading pie graph...')
    trace = graph_objs.Pie(labels=labels, values=values)

    plotly.plot([trace], filename='movies_pie_chart', open=True)
