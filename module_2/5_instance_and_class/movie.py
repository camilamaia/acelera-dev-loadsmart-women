import time
import webbrowser


class Movie:
    # Class attribute
    is_media = True

    # Class method
    @classmethod
    def definition(cls):
        print('A movie is a series of still images that, when shown on a screen, create the '
              'illusion of moving images')

    # Instance attributes
    def __init__(self, title, stars, director, trailer_url):
        self.title = title
        self.stars = stars
        self.director = director
        self.trailer_url = trailer_url

    # Instance method
    def print_specifications(self):
        print('\nMOVIE: {}'.format(self.title))
        time.sleep(2)
        print('STARS: {}'.format(self.stars))
        time.sleep(2)
        print('DIRECTOR: {}'.format(self.director))
        time.sleep(2)

    # Instance method
    def show_trailer(self):
        print('\nLoading {} trailer...'.format(self.title))
        webbrowser.open_new(self.trailer_url)
        time.sleep(10)


black_panther = Movie(
    'Black Panther',
    ['Chadwick Boseman', 'Michael B. Jordan', "Lupita Nyong'o"],
    'Ryan Coogler',
    'https://www.youtube.com/watch?v=dxWvtMOGAhw',
)


print(Movie.is_media)
Movie.definition()
print(black_panther.title)
black_panther.print_specifications()
