from plotly import tools, plotly, graph_objs
import time

from movie import Movie
from charts import plot_pie


def movies():
    black_panther = Movie(
        'Black Panther',
        ['Chadwick Boseman', 'Michael B. Jordan', "Lupita Nyong'o"],
        'Ryan Coogler',
        'https://www.youtube.com/watch?v=dxWvtMOGAhw',
        30
    )

    green_book = Movie(
        'Green Book',
        ['Viggo Mortensen', 'Mahershala Ali', 'Linda Cardellini'],
        'Peter Farrelly',
        'https://www.youtube.com/watch?v=uC-_Gon2p9M',
        23
    )

    bohemian_rhapsody = Movie(
        'Bohemian Rhapsody',
        ['Rami Malek', 'Lucy Boynton', 'Gwilym Lee'],
        'Bryan Singer',
        'https://www.youtube.com/watch?v=GryRsVhOvxo',
        20
    )

    return [black_panther, green_book, bohemian_rhapsody]


def present_top_3(movies):
    print('AceleraDev Presenting...')
    time.sleep(2)
    print('TOP 3 2019 OSCAR MOVIES')
    time.sleep(2)

    for movie in movies:
        movie.print_specifications()
        movie.show_trailer()


def present_results(movies):
    print('\nAnd the results are...')
    time.sleep(2)

    labels = []
    values = []

    for movie in movies:
        movie.print_votes()
        labels.append(movie.title)
        values.append(movie.votes)

    print("\nLet's see a graph with the results!")

    plot_pie(labels, values)


movies = movies()
present_top_3(movies)
present_results(movies)
