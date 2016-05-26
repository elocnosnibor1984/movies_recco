from system.core.controller import *
from itertools import groupby
import json, requests
from twilio.rest import TwilioRestClient
from flask import request

account_sid = "AC82feb6eb3602630d15a0fab23b0db269" # Your Account SID from www.twilio.com/console
auth_token  = "8c6d71dd5574672863abe6dceb31dac8"  # Your Auth Token from www.twilio.com/console
client = TwilioRestClient(account_sid, auth_token)

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
            if title != "Star Wars " and title != "Return of the Jedi ":
                resp = requests.get('http://www.omdbapi.com/?t='+title+'&y=&plot=short&r=json')
                movie_list.append(json.loads(resp.text))
        return self.load_view('Movie_Dashboard/watchpopular_movie.html', watched_movies=watched_movies, movie_list=movie_list)

    def logout(self):
        session.pop();
        return redirect('/')

    def add_friend(self):
        return self.load_view('Movie_Dashboard/add_friends.html')

    def send_to_someone(self):
        title=request.form['title']
        review=request.form['review']
        review = title + " : " + review
        user_id = 1
        friends = self.models['Movie_model'].get_friends(user_id)
        return self.load_view('movie_dashboard/send_to_someone.html', review=review, friends=friends)

    def send_sms(self):
        new_message=request.form['review']
        new_number=request.form.getlist('number')
        print "new number: ", new_number
        for x in new_number:
            x = "+"+"1"+str(x)+""
            x = str(x)
            message = client.messages.create(body=new_message,
                to=x,    # Replace with your phone number
                from_="+14083378347") # Replace with your Twilio number
        print(message.sid)
        return redirect("/")
