from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# For bcrypt
from flask_app import app # Import the app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Link models as needed in your projects!
from flask_app.models import relic

class User:
    db_name = "users_schema_may_2022" # Class variable holding the schema we're accessing 
    def __init__(self, data): # data is a dictionary representing a record (row) from your database
        self.id = data["id"] # Column names must match from yhour database
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.relics = [] #placeholder holding a bunch of relics 
        # self.??? = None or []

    @classmethod
    def register_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def grab_one_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0:
            return None
        else:
            return cls(results[0])

    @classmethod
    def grab_one_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0:
            return None
        else:
            return cls(results[0])

    @classmethod
    def grab_all_relics_by_user(cls, data):
        query = "SELECT * FROM users LEFT JOIN relics ON users.id = relics.user_id WHERE users.id = %(id)s;" #start from users because some users might not have posts at all
        #this is similar to when we are getting one relic with user 
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0:
            return []
        else:
            #create the user -- [copy and paste all relic instances [] code ]
            user_instance = cls(results[0])
            #go through each relic 
            #loop through each relic from the query - go through each dictionary
            for current_relic_dictionary in results:
                #create a relic class instance
                #relic_instance = cls(current_relic_dictionary)
                #grab the info about the relic in its own dictionary
                new_relic_dictionary = {
                    "id": current_relic_dictionary["relics.id"], # Column names must match from yhour database
                    "name": current_relic_dictionary["name"],
                    "discovery_date": current_relic_dictionary["discovery_date"],
                    "description": current_relic_dictionary["description"],
                    "created_at": current_relic_dictionary["relics.created_at"],
                    "updated_at": current_relic_dictionary["relics.updated_at"]
                }
                #create the relic
                relic_instance = relic.Relic(new_relic_dictionary)
                #add this relic to the list
                user_instance.relics.append(relic_instance)
            #return user with relics 
            return user_instance



            
    # You will use staticmethods to perform your validations
    @staticmethod
    def validate_new_user(form_data):
        is_valid = True # Assume everything is good to start
        # Check each field individually
        if len(form_data["first_name"]) < 3:
            is_valid = False
            flash("First name must be at least 3 characters.", "register")
        if len(form_data["last_name"]) < 3:
            is_valid = False
            flash("Last name must be at least 3 characters.", "register")
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Email address is not formatted correctly.", "register")
            is_valid = False
        if len(form_data["password"]) < 8:
            is_valid = False
            flash("Password must be at least 8 characters.", "register")
        if not form_data["password"] == form_data["confirm_password"]:
            is_valid = False
            flash("Passwords do not match.", "register")
        return is_valid

    @staticmethod
    def validate_login(form_data):
        is_valid = True
        # Check to see if someone even has that email in the database
        email_data = {
            "email": form_data["email"]
        }
        found_user_or_none = User.grab_one_user_by_email(email_data)
        if not found_user_or_none:
            flash("Invalid login credentials.", "login")
            return False # Stop validations here - no need to check password
        # Check the password ONLY IF the user has been found with that email
        if not bcrypt.check_password_hash(found_user_or_none.password, form_data['password']):
            flash("Invalid login credentials.", "login")
            is_valid = False
        return is_valid