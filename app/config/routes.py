
from system.core.router import routes


routes['default_controller'] = 'Access_controller'
routes['GET']['/Login_Registration'] = 'Users_controller#Login_Registration'
routes['POST']['/process_registration'] = 'Users_controller#process_registration'
routes['POST']['/process_login'] = 'Users_controller#process_login'
routes['GET']['/update_user'] = 'Users_controller#update_user'
routes['GET']['/All_movie_display'] = 'Movie_controller#display_all_movies'
routes['GET']['/most_popular_movies'] = 'Movie_controller#most_popular_movies'
routes['GET']['/most_watched_movies'] = 'Movie_controller#most_watched_movies'
routes['GET']['/add_friends'] = 'Movie_controller#add_friend'
routes['GET']['/logout'] = 'Users_controller#logout'
routes['POST']['/send_to_someone'] = 'Movie_controller#send_to_someone'
routes['POST']['/send_sms'] = 'Movie_controller#send_sms'


# temporary routes
routes['GET']['/movie_dashboard'] = 'Users_controller#movie_dashboard'
routes['GET']['/add_review'] = 'Users_controller#add_review'
