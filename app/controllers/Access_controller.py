
from system.core.controller import *
from itertools import groupby

class Access_controller(Controller):
    def __init__(self, action):
        super(Access_controller, self).__init__(action)

        self.db = self._app.db
        # self.load_model('Users_model')

    def index(self):
        return self.load_view('Home.html')
