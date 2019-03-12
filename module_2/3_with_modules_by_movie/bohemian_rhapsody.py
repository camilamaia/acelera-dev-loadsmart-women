import time
import webbrowser


def print_specifications():
    print('\nMOVIE: Bohemian Rhapsody')
    time.sleep(2)
    print('STARS: Rami Malek, Lucy Boynton, Gwilym Lee')
    time.sleep(2)
    print('DIRECTOR: Bryan Singer')
    time.sleep(2)


def show_trailer():
    print('\nLoading Bohemian Rhapsody trailer...')
    webbrowser.open_new('https://www.youtube.com/watch?v=GryRsVhOvxo')
    time.sleep(10)


def print_votes():
    print('\nBohemian Rhapsody')
    time.sleep(2)
    print('20 votes')
    time.sleep(2)
