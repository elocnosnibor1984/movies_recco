from system.core.controller import *
from itertools import groupby

class Movie_controller(Controller):
    def __init__(self, action):
        super(Movie_controller, self).__init__(action)

        self.db = self._app.db
        self.load_model('Users_model')
        self.load_model('Movie_model')

    def display_all_movies(self):
        all_movies = self.models['Movie_model'].get_all_movies()

        return self.load_view('Movie_Dashboard/all_movies.html', all_movies = all_movies)
