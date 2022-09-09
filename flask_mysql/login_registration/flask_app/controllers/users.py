from ast import Pass
from flask_app import app # Import the app
# Add bcrypt for hashing passwords when registering
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask import render_template, request, redirect, session, flash
from flask_app.models import user, relic
# Visible routes
@app.route("/")
def index_route():
    return render_template("login_reg.html")

@app.route("/dashboard")
def dashboard():
    # One way to check if someone is logged in
    if "user_id" in session: # Only show this HTML file if someone is logged in
        data = {
            "id": session["user_id"]
        }
        # Grab the user who's logged in AND show this HTML file
        return render_template("dashboard.html", this_user = user.User.grab_one_user_by_id(data), all_relics = relic.Relic.get_all_relics_with_users(data))
    else: # Send client back who's not logged in
        return redirect("/")
    """ Another way to check to see if someone is NOT logged in
    if "user_id" not in session:
        return redirect("/")
    return render_template("")
    """
    

@app.route("/my_relics")
def user_relics():
    #check to see if someone is not logged in if not send to the login page
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": session["user_id"],
    }
    return render_template("my_relic.html", this_user = user.User.grab_all_relics_by_user(data)) #to grab all relics from one user 

#@app.route("/new_route")
#def new_route():
#    # Another way to show if someone is logged in - in this case, NOT logged in
#    if "user_id" not in session:
#        return redirect("/")
#    return render_template("new_page.html")



# INVISIBLE routes

# Register a new user
@app.route("/register", methods=["POST"])
def register_user():
    # Validate the form first
    # If the validations fail, go back to the previous route
    if not user.User.validate_new_user(request.form):
        return redirect("/")
    else: # Validations succeed
        # Remember to hash the passworD!!1
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password": bcrypt.generate_password_hash(request.form['password']), # HASH THE PASSWORD!!!!
        }
        # Call on the model to register the new user - save the ID of the user in session so we know who's logged in
        session["user_id"] = user.User.register_user(data)
        # Redirect to the dashboard
        return redirect('/dashboard')

# Login an existing user
@app.route("/login", methods=["POST"])
def login_user():
    # Validate the form first
    # If the validations fail, go back to the previous route
    if not user.User.validate_login(request.form):
        return redirect("/")
    else:
        # Grab the user from the database
        email_data = {
            "email": request.form["email"]
        }
        found_user = user.User.grab_one_user_by_email(email_data)
        # Save the ID in session
        session["user_id"] = found_user.id
        return redirect("/dashboard")

@app.route("/logout")
def logout(): # Clear session, THEN send to the registration/login page via the root route
    session.clear()
    return redirect("/")
