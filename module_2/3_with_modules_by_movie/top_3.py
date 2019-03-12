from charts import plot_pie
import time

import black_panther
import bohemian_rhapsody
import green_book


def present_top_3():
    print('AceleraDev Presenting...')
    time.sleep(2)
    print('TOP 3 2019 OSCAR MOVIES')
    time.sleep(2)

    black_panther.print_specifications()
    black_panther.show_trailer()

    green_book.print_specifications()
    green_book.show_trailer()

    bohemian_rhapsody.print_specifications()
    bohemian_rhapsody.show_trailer()


def present_results():
    print('\nAnd the results are...')
    time.sleep(2)

    bohemian_rhapsody.print_votes()
    green_book.print_votes()
    black_panther.print_votes()

    print("\nLet's see a graph with the results!")

    labels = ['Black Panther', 'Green Book', 'Bohemian Rhapsody', 'Others']
    values = [30, 23, 20, 15]

    plot_pie(labels, values)


present_top_3()
present_results()
