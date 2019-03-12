import time
import webbrowser
from plotly import tools, plotly, graph_objs


def present_top_3():
    print('AceleraDev Presenting...')
    time.sleep(2)
    print('TOP 3 2019 OSCAR MOVIES')
    time.sleep(2)

    print('\nMOVIE: Black Panther')
    time.sleep(2)
    print("STARS: Chadwick Boseman, Michael B. Jordan, Lupita Nyong'o")
    time.sleep(2)
    print('DIRECTOR: Ryan Coogler')
    time.sleep(2)

    print('\nLoading Black Panther trailer...')
    webbrowser.open_new('https://www.youtube.com/watch?v=dxWvtMOGAhw')
    time.sleep(10)

    print('\nMOVIE: Green Book')
    time.sleep(2)
    print('STARS: Viggo Mortensen, Mahershala Ali, Linda Cardellini')
    time.sleep(2)
    print('DIRECTOR: Peter Farrelly')
    time.sleep(2)

    print('\nLoading Green Book trailer...')
    webbrowser.open_new('https://www.youtube.com/watch?v=uC-_Gon2p9M')
    time.sleep(10)

    print('\nMOVIE: Bohemian Rhapsody')
    time.sleep(2)
    print('STARS: Rami Malek, Lucy Boynton, Gwilym Lee')
    time.sleep(2)
    print('DIRECTOR: Bryan Singer')
    time.sleep(2)

    print('\nLoading Bohemian Rhapsody trailer...')
    webbrowser.open_new('https://www.youtube.com/watch?v=GryRsVhOvxo')
    time.sleep(10)


def present_results():
    print('\nAnd the results are...')
    time.sleep(2)

    print('\nBohemian Rhapsody')
    time.sleep(2)
    print('20 votes')
    time.sleep(2)

    print('\nGreen Book')
    time.sleep(2)
    print('23 votes')
    time.sleep(2)

    print('\nBlack Panther')
    time.sleep(2)
    print('30 votes')
    time.sleep(2)

    print("\nLet's see a graph with the results!")

    labels = ['Black Panther', 'Green Book', 'Bohemian Rhapsody']
    values = [30, 23, 20]

    plot_pie(labels, values)


def plot_pie(labels, values):
    print('\nLoading pie graph...')

    # authenticate with your credentials:
    # tools.set_credentials_file(username='', api_key='')

    trace = graph_objs.Pie(labels=labels, values=values)
    plotly.plot([trace], filename='movies_pie_chart', open=True)


present_top_3()
present_results()
