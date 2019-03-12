from charts import plot_pie
import time
import movies


def present_top_3():
    print('AceleraDev Presenting...')
    time.sleep(2)
    print('TOP 3 2019 OSCAR MOVIES')
    time.sleep(2)

    movies.print_specifications(
        'Black Panther',
        ['Chadwick Boseman', 'Michael B. Jordan', "Lupita Nyong'o"],
        'Ryan Coogler',
    )
    movies.show_trailer(
        'Black Panther', 'https://www.youtube.com/watch?v=dxWvtMOGAhw'
    )

    movies.print_specifications(
        'Green Book',
        ['Viggo Mortensen', 'Mahershala Ali', 'Linda Cardellini'],
        'Peter Farrelly'
    )
    movies.show_trailer(
        'Green Book', 'https://www.youtube.com/watch?v=uC-_Gon2p9M'
    )

    movies.print_specifications(
        'Bohemian Rhapsody',
        ['Rami Malek', 'Lucy Boynton', 'Gwilym Lee'],
        'Bryan Singer'
    )
    movies.show_trailer(
        'Bohemian Rhapsody', 'https://www.youtube.com/watch?v=GryRsVhOvxo'
    )


def present_results():
    print('\nAnd the results are...')
    time.sleep(2)

    movies.print_votes('Bohemian Rhapsody', 20)
    movies.print_votes('Green Book', 23)
    movies.print_votes('Black Panther', 30)

    print("\nLet's see a graph with the results!")

    labels = ['Black Panther', 'Green Book', 'Bohemian Rhapsody', 'Others']
    values = [30, 23, 20, 15]

    plot_pie(labels, values)


present_top_3()
present_results()
