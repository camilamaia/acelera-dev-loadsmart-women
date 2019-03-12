import time
import webbrowser


class Movie:
    def __init__(self, title, stars, director, trailer_url):
        self.title = title
        self.stars = stars
        self.director = director
        self.trailer_url = trailer_url

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


class KidsMovie(Movie):
    def __init__(self, title, stars, director, trailer_url, recommended_age):
        super().__init__(title, stars, director, trailer_url)
        self.recommended_age = recommended_age

    def show_recommended_age(self):
        print('\nThis movie is mainly recommended for kids from {} to {} years'.format(
            self.recommended_age.start,
            self.recommended_age.stop
        ))

    def show_trailer(self):
        self.show_recommended_age()
        super().show_trailer()


my_neighbor_totoro = KidsMovie(
    'My Neighbor Totoro',
    ['Hitoshi Takagi', 'Noriko Hidaka', 'Chika Sakamoto'],
    'Hayao Miyazaki',
    'https://www.youtube.com/watch?v=TuLX50_5UAI',
    range(0,10)
)

my_neighbor_totoro.show_trailer()
