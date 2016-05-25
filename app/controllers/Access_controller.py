
from system.core.controller import *
from itertools import groupby
from twilio.rest import TwilioRestClient

account_sid = "AC82feb6eb3602630d15a0fab23b0db269" # Your Account SID from www.twilio.com/console
auth_token  = "8c6d71dd5574672863abe6dceb31dac8"  # Your Auth Token from www.twilio.com/console
client = TwilioRestClient(account_sid, auth_token)

class Access_controller(Controller):
    def __init__(self, action):
        super(Access_controller, self).__init__(action)

        self.db = self._app.db
        # self.load_model('Users_model')

    def index(self):
        return self.load_view('Home.html')

    def find_movie(self):
        return self.load_view('Home.html')

    def send_to_someone(self):
    	title=request.form['title']
    	review=request.form['review']
    	review = title + " : " + review
        return self.load_view('movie_dashboard/send_to_someone.html', review=review)

    def send_sms(self):
    	new_message=request.form['review']
        new_number=request.form['number']
        print new_number
        new_number="+"+new_number
        print new_number
        new_number=str(new_number)
        message = client.messages.create(body=new_message,
            to=new_number,    # Replace with your phone number
            from_="+14083378347") # Replace with your Twilio number

        print(message.sid)
        # return self.load_view('Home.html')
        return redirect("/")
