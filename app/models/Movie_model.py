"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Movie_model(Model):
    def __init__(self):
        super(Movie_model, self).__init__()

    def get_all_movies(self):
        query = "SELECT movie_tile, imdb_url FROM movies"
        return self.db.query_db(query)

    def most_popular_movies(self):
        query = "SELECT movies.movie_tile as movie, most_popular_movie.total_rating as rating FROM most_popular_movie LEFT JOIN movies ON most_popular_movie.movie_id = movies.idmovies ORDER BY most_popular_movie.total_rating DESC  LIMIT 50"
        return self.db.query_db(query)

    def most_watched_movies(self):
        query = query = "SELECT movies.movie_tile as movie, most_watched_movie.total_watched as total_watched FROM most_watched_movie LEFT JOIN movies ON most_watched_movie.movie_id = movies.idmovies ORDER BY most_watched_movie.total_watched DESC LIMIT 50"
        return self.db.query_db(query)

    def get_friends(self, user_id):
        query="Select * from friends where user_id=:user_id"
        data = {'user_id':user_id}
        return self.db.query_db(query,data)


    """
    Below is an example of a model method that queries the database for all users in a fictitious application

    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True

    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """
