import time
import webbrowser


def print_specifications():
    print('\nMOVIE: Black Panther')
    time.sleep(2)
    print("STARS: Chadwick Boseman, Michael B. Jordan, Lupita Nyong'o")
    time.sleep(2)
    print('DIRECTOR: Ryan Coogler')
    time.sleep(2)


def show_trailer():
    print('\nLoading Black Panther trailer...')
    webbrowser.open_new('https://www.youtube.com/watch?v=dxWvtMOGAhw')
    time.sleep(10)


def print_votes():
    print('\nBlack Panther')
    time.sleep(2)
    print('30 votes')
    time.sleep(2)
