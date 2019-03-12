import time
import webbrowser


def print_specifications(title, stars, director):
    print('\nMOVIE: {}'.format(title))
    time.sleep(2)
    print('STARS: {}'.format(stars))
    time.sleep(2)
    print('DIRECTOR: {}'.format(director))
    time.sleep(2)


def show_trailer(title, url):
    print('\nLoading {} trailer...'.format(title))
    webbrowser.open_new(url)
    time.sleep(10)


def print_votes(title, number_of_votes):
    print('\n{}'.format(title))
    time.sleep(2)
    print("{} votes".format(number_of_votes))
    time.sleep(2)
