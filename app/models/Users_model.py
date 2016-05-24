
from system.core.model import Model
import re

class Users_model(Model):
    def __init__(self):
        super(Users_model, self).__init__()
# Inserting usrs if all info is correct
    def create_user(self, user_info):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
        # PASSWORD_REGEX = re.compile(r'^[A-Z\d]*$')
        errors = []
        # Check for first name
        if user_info['first_name'] == "":
            errors.append("First name cannot be empty")

        elif any(char.isdigit() for char in user_info['first_name']) == True:
            errors.append("Name cannot have digits")

        else:
            print "name correct"
        # Check for last name
        if user_info['last_name'] == "":
            errors.append("First name cannot be empty")
        elif any(char.isdigit() for char in user_info['last_name']) == True:
            erros.append("Name cannot have digits")
        else:
            print "Name is correct"
        # check for email
        if user_info['email'] == "":
            errors.append("email cannot be empty")

        elif not EMAIL_REGEX.match(user_info['email']):
            errors.append("Invalid email address")
        else:
            print "email is correct"
        # check for passowrd
        if user_info['password'] == "":
            errors.append("Password cannot be empty")
        else:
            print "Password is correct"

        # confirm_password validation
        if user_info['confirm_password'] == "":
            errors.append("Please confirm passowrd")

        elif user_info['confirm_password']!= user_info['password']:
            errors.append("password do not match")

        else:
            print"Passeword matches"

        if errors:
            return {"status": False, "errors": errors}
        else:
            # inserting userProfile
            print "hi"
            password = user_info['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)
            query = "INSERT INTO users(first_name, last_name, email,  password,  created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, NOW(), NOW())"
            values = {
                'first_name': user_info['first_name'],
                'last_name': user_info['last_name'],
                'email': user_info['email'],
                'password': hashed_pw,

            }
            self.db.query_db(query, values)
            # This query will retieve the last inserted user
            query = "SELECT * from users ORDER By idusers DESC LIMIT 1"
            user = self.db.query_db(query)
            print "Users retieve"
            return {"status": True, "user": user[0]}

    def login_user(self, user_info):
        password = user_info['password']
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        values = {'email': user_info['email']}
        user = self.db.query_db(query, values)
        print user
        if user:
            # pw_hash = self.bcrypt.generate_password_hash(password)
            if user[0]['password']==password:
                return {"status": True, "user":user[0]}
            else:
                return {"status": False}
        else:
            return {"status": False}
    def get_All_users(self):
        query = "SELECT * FROM users"
        return  self.db.query_db(query)

    def create_user_Byadmin(self, user_info):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    # PASSWORD_REGEX = re.compile(r'^[A-Z\d]*$')
        errors = []
    # Check for first name
        if user_info['first_name'] == "":
            errors.append("First name cannot be empty")

        elif any(char.isdigit() for char in user_info['first_name']) == True:
            errors.append("Name cannot have digits")

        else:
            print "name correct"
    # Check for last name
        if user_info['last_name'] == "":
            errors.append("First name cannot be empty")
        elif any(char.isdigit() for char in user_info['last_name']) == True:
            erros.append("Name cannot have digits")
        else:
            print "Name is correct"
    # check for email
        if user_info['email'] == "":
            errors.append("email cannot be empty")

        elif not EMAIL_REGEX.match(user_info['email']):
            errors.append("Invalid email address")
        else:
            print "email is correct"
    # check for passowrd
        if user_info['password'] == "":
            errors.append("Password cannot be empty")
        else:
            print "Password is correct"

    # confirm_password validation
        if user_info['confirm_password'] == "":
            errors.append("Please confirm passowrd")

        elif user_info['confirm_password']!= user_info['password']:
            errors.append("password do not match")

        else:
            print"Passeword matches"

        if errors:
            return {"status": False, "errors": errors}
        else:
        # inserting userProfile
            print "hi"
            password = user_info['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)
            query = "INSERT INTO users(first_name, last_name, email,  password, user_level, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password,:user_level, NOW(), NOW())"
            values = {
                'first_name': user_info['first_name'],
                'last_name': user_info['last_name'],
                'email': user_info['email'],
                'password': hashed_pw,
                'user_level': 'normal'
                }
            self.db.query_db(query, values)
        # This query will retieve the last inserted user
        # query = "SELECT * from users ORDER By idusers DESC LIMIT 1"
        # user = self.db.query_db(query)
            print "Users retieve"
            return {"status": True}

    def getuser_ById(self, user_id):
        query = "SELECT * FROM users WHERE idusers = :idusers"
        values = {'idusers': user_id}
        return self.db.query_db(query, values)

    def get_all_users(self):
        query = "SELECT * FROM users"
        return self.db.query_db(query)

        # if user:
        #     # check_password_hash() compares encrypted password in DB to one provided by user logging in
        #     pw_hash = self.bcrypt.generate_password_hash(password)
        #     if self.bcrypt.check_password_hash(user[0]['password'], pw_hash):
        #         return {user:user[0]}







        # Whether we did not find the email, or if the password did not match, either way return False



    """
    def
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
