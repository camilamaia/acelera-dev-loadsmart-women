import time
import webbrowser


class Movie:
    def __init__(self, title, stars, director, trailer_url, votes):
        self.title = title
        self.stars = stars
        self.director = director
        self.trailer_url = trailer_url
        self.votes = votes

    def print_specifications(self):
        print('\nMOVIE: {}'.format(self.title))
        time.sleep(2)
        print('STARS: {}'.format(self.stars))
        time.sleep(2)
        print('DIRECTOR: {}'.format(self.director))
        time.sleep(2)

    def show_trailer(self):
        print('\nLoading {} trailer...'.format(self.title))
        webbrowser.open_new(self.trailer_url)
        time.sleep(10)

    def print_votes(self):
        print('\n{}'.format(self.title))
        time.sleep(2)
        print("{} votes".format(self.votes))
        time.sleep(2)
