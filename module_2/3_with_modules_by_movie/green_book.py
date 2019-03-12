import time
import webbrowser


def print_specifications():
    print('\nMOVIE: Green Book')
    time.sleep(2)
    print('STARS: Viggo Mortensen, Mahershala Ali, Linda Cardellini')
    time.sleep(2)
    print('DIRECTOR: Peter Farrelly')
    time.sleep(2)


def show_trailer():
    print('\nLoading Green Book trailer...')
    webbrowser.open_new('https://www.youtube.com/watch?v=uC-_Gon2p9M')
    time.sleep(10)


def print_votes():
    print('\nGreen Book')
    time.sleep(2)
    print('23 votes')
    time.sleep(2)
