
from system.core.controller import *
from itertools import groupby
import requests, json

class Users_controller(Controller):
    def __init__(self, action):
        super(Users_controller, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.db = self._app.db
        # self.load_model('Users_model')
        # self.load_model('Book_model')
        # self.load_model('Review_model')
        # self.load_model('Author_model')
        # self.load_model('Dashboard_model')

    def Login_Registration(self):
        return self.load_view('Users/Login_Registration.html')

    def process_registration(self):
        user_info = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'password': request.form['password'],
                'confirm_password': request.form['confirm_password']
        }
        create_status = self.models['Users_model'].create_user(user_info)
        print create_status
        if create_status['status'] == True:
            session['idusers'] = create_status['user']['idusers']
            session['first_name'] = create_status['user']['first_name']
            # redirect('Users/userProfile.html')
            return redirect('/')
        else:
            for message in create_status['errors']:
                flash(message, 'regis_erros')
            return redirect('/')
        return self.load_view('Book_Dashboard/Book_Information.html')

    # Login prcooess here
    def process_login(self):
        user_info = {
                'email': request.form['email'],
                'password': request.form['password'],
                }
        create_status = self.models['Users_model'].login_user(user_info)
        print create_status
        if create_status['status'] == False:
            return redirect('/')
        else:
            session['idusers'] = create_status['user']['idusers']
            session['first_name'] = create_status['user']['first_name']
            recent_book_reviews = self.models['Review_model'].get_all_reviews()
            all_books = self.models['Book_model'].get_all_books()
            all_users = self.models['Users_model'].get_all_users()
            # get_all_stuff = self.models['Review_model'].get_all_stuff()
            # print get_all_stuff
            return self.load_view('Book_Dashboard/Book_Information.html',recent_book_reviews = recent_book_reviews, all_books= all_books, all_users = all_users  )


        #  update user in database
    def update_user(self):
        return self.load_view('Users/update_user.html')

    def movie_dashboard(self):
        # arr=['Aladdin', 'Beauty and the Beast', 'Sword in the Stone', 'Princess and the Frog', 'Cinderella', 'Lion King']
        # arr = str(arr)
        # file = open("data.txt", "w")
        # file.write(arr)
        # file.close()
        movie_list=[]
        movies=["Batman", "Troll 2", "The Shining"]
        for x in range(len(movies)):
            resp = requests.get('http://www.omdbapi.com/?t='+movies[x]+'&y=&plot=short&r=json')
            movie_list.append(json.loads(resp.text))
        return self.load_view('Movie_Dashboard/movie_userdashboard.html', movie_list=movie_list)

    def add_review(self):
        return self.load_view('Movie_Dashboard/add_review_text.html')
