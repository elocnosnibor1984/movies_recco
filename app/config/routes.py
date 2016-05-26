
from system.core.router import routes


routes['default_controller'] = 'Access_controller'
routes['GET']['/Login_Registration'] = 'Users_controller#Login_Registration'
routes['POST']['/process_registration'] = 'Users_controller#process_registration'
routes['POST']['/process_login'] = 'Users_controller#process_login'
routes['GET']['/update_user'] = 'Users_controller#update_user'
routes['GET']['/All_movie_display'] = 'Movie_controller#display_all_movies'
routes['GET']['/most_popular_movies'] = 'Movie_controller#most_popular_movies'
routes['GET']['/most_watched_movies'] = 'Movie_controller#most_watched_movies'
routes['GET']['/logout'] = 'Users_controller#logout'

# temporary routes
routes['GET']['/movie_dashboard'] = 'Users_controller#movie_dashboard'
routes['GET']['/add_review'] = 'Users_controller#add_review'
