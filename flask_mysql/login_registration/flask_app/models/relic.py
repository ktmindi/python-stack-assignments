from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
#EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# For bcrypt
from flask_app import app # Import the app
#from flask_bcrypt import Bcrypt
#bcrypt = Bcrypt(app)

#link models as needed in your projects!
from flask_app.models import user

class Relic:
    db_name = "users_schema_may_2022" # Class variable holding the schema we're accessing 
    def __init__(self, data): # data is a dictionary representing a record (row) from your database
        self.id = data["id"] # Column names must match from yhour database
        self.name = data["name"]
        self.discovery_date = data["discovery_date"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None #placeholder holding a bunch of relics 
        # self.??? = None or []

# add relic to data base
    @classmethod
    def add_relic(cls,data):
        query = "INSERT INTO relics (name, description, discovery_date, user_id) VALUES (%(name)s, %(description)s, %(discovery_date)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

#grab all relics with who added them
    @classmethod
    def get_all_relics_with_users(cls, data):
        query = "SELECT * FROM relics JOIN users ON relics.user_id = users.id;"
        results = connectToMySQL(cls.db_name).query_db(query)  #dont need to put in data because its not relying on grabbing data
        print(results)
        if len(results) == 0:
            return[]
        else:
            all_relic_instances = [] #hold all your relics new class
            #loop through each relic from the query - go through each dictionary
            for current_relic_dictionary in results:
                #create a relic class instance
                relic_instance = cls(current_relic_dictionary)
                #grab the info about the user who  made it in its own dictionary
                new_user_dictionary = {
                    "id": current_relic_dictionary["users.id"], #column names much match database
                    "first_name": current_relic_dictionary["first_name"],
                    "last_name": current_relic_dictionary["last_name"],
                    "email": current_relic_dictionary["email"],
                    "password": current_relic_dictionary["password"],
                    "created_at": current_relic_dictionary["users.created_at"],
                    "updated_at": current_relic_dictionary["users.updated_at"], #must add table name because we are joining tables and the table is being used more than once
                }
                #create user class instance
                user_instance = user.User(new_user_dictionary)
                #link this user to this relic
                relic_instance.user = user_instance
                #add this relic to the list called all_relic_instances
                all_relic_instances.append(relic_instance)
            return all_relic_instances


#grab one relic -- first copy and paste the grab all relics with who added them and make changes
    @classmethod
    def get_one_relic_with_user(cls, data):
        query = "SELECT * FROM relics JOIN users ON relics.user_id = users.id WHERE relics.id= %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)  #need to put data because its relying on the table to get the data
        print(results)
        if len(results) == 0:
            return[]
        else:
            this_relic_instance = cls(results[0]) #hold all your relics new class
            #loop through each relic from the query - go through each dictionary
            #dont need for loop because we are only grabbing one for current_relic_dictionary in results:
                #create a relic class instance
                #relic_instance = cls(current_relic_dictionary)
                #grab the info about the user who  made it in its own dictionary
            new_user_dictionary = {
                "id": results[0]["users.id"], #column names much match database
                "first_name": results[0]["first_name"],
                "last_name": results[0]["last_name"],
                "email": results[0]["email"],
                "password": results[0]["password"],
                "created_at": results[0]["users.created_at"],
                "updated_at": results[0]["users.updated_at"], #must add table name because we are joining tables and the table is being used more than once
            }
                #create user class instance
            user_instance = user.User(new_user_dictionary)
                #link this user to this relic
            this_relic_instance.user = user_instance
                #add this relic to the list called this_relic instance
                # dont need append anymore this_relic_instance.append(relic_instance)
            return this_relic_instance


#edit relic
    @classmethod
    def edit_relic(cls, data):
        query = "UPDATE relics SET name = %(name)s, discovery_date = %(discovery_date)s, description = %(description)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)


#copy edit relic and change it to delete relic
    @classmethod
    def delete_relic(cls, data):
        query = "DELETE FROM relics WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

# need to add validation for create function

    @staticmethod
    def validate_relic(relic_data):
        is_valid = True
        #name is long enough?
        if len(relic_data["name"]) < 4:
            flash("Name must be 4 or more characters.", "relic")
            is_valid = False
        #is a date present
        if relic_data["discovery_date"] == '':
            flash("Must enter a discovery date", "relic")
            is_valid = False
        #description is long enough?
        if len(relic_data["description"]) < 10:
            flash("Description must be 10 or more characters.", "relic")
            is_valid = False
        return is_valid