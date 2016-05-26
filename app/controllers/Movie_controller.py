from system.core.controller import *
from itertools import groupby
import json, requests

class Movie_controller(Controller):
    def __init__(self, action):
        super(Movie_controller, self).__init__(action)

        self.db = self._app.db
        self.load_model('Users_model')
        self.load_model('Movie_model')

    def display_all_movies(self):
        all_movies = self.models['Movie_model'].get_all_movies()

        return self.load_view('Movie_Dashboard/all_movies.html', all_movies = all_movies)

    def most_popular_movies(self):
        popular_movies = self.models['Movie_model'].most_popular_movies()
        movie_list=[]
        for x in range(len(popular_movies)):
            movie = popular_movies[x]['movie']
            title = movie[:-6]
            if title[-6]== ',':
                cut_the=title[:-6]
                title="The "+ cut_the
            if title != "Star Wars " and title != "Return of the Jedi ":
                resp = requests.get('http://www.omdbapi.com/?t='+title+'&y=&plot=short&r=json')
                movie_list.append(json.loads(resp.text))
        return self.load_view('Movie_Dashboard/popular_movies.html', movie_list=movie_list, popular_movies=popular_movies)

    def most_watched_movies(self):
        watched_movies = self.models['Movie_model'].most_watched_movies()
        movie_list=[]
        for x in range(len(watched_movies)):
            movie = watched_movies[x]['movie']
            title = movie[:-6]
            if "The" in title:
                title= "The "+ title[:-6]
            # if len(title)>6:
            #     if title[-6]== ',':
            #         cut_the=title[:-6]
            #         title="The "+ cut_the
            if title != "Star Wars " and title != "Return of the Jedi ":
                resp = requests.get('http://www.omdbapi.com/?t='+title+'&y=&plot=short&r=json')
                movie_list.append(json.loads(resp.text))
        return self.load_view('Movie_Dashboard/watchpopular_movie.html', watched_movies=watched_movies, movie_list=movie_list)

    def logout(self):
        session.pop();
        return redirect('/')
