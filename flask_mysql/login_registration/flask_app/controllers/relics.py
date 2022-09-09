from flask_app import app # Import the app
# Add bcrypt for hashing passwords when registering
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask import render_template, request, redirect, session, flash
from flask_app.models import user,relic

#VISIBLE ROUTES
@app.route("/relics/new")
def new_relic_page():
    #check to see if someone is not logged in if not send to the login page
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": session["user_id"],  #this id must match what it says in users.py
    }
    return render_template("add_relic.html", this_user = user.User.grab_one_user_by_id(data))

@app.route("/relics/<int:id>/edit")
def edit_relic_page(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": id #id of the relic not the id of the user
    }
    # you dont need to use the same method to grab a relic - you could write a new method to grab without 
    # the user, but we'll reuse the method to grab a relic with the user to save time
    return render_template("edit_relic.html", this_relic = relic.Relic.get_one_relic_with_user(data))

@app.route("/relics/<int:id>")
def  view_relic_page(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": id #id of the relic not the id of the user
    }
    return render_template("view_relic.html", this_relic = relic.Relic.get_one_relic_with_user(data))

#invisible routes
@app.route("/relics/<int:id>/delete")
def delete_relic(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": id,
    }
    relic.Relic.delete_relic(data)
    return redirect ("/dashboard")

@app.route("/relics/add_relic_to_db", methods=["POST"])
def add_relic_to_db():
    #check to see if someone is not logged in if not send to the login page MOST ROUTES NEED THIS EXCEPT FOR LOGIN ROUTES
    if "user_id" not in session:
        return redirect("/")
    # validate first
    if not relic.Relic.validate_relic(request.form): #if relic fails where are we redirecting
        return redirect("/relics/new") #always redirect back to previous route 
    else:
        #ADD THIS RELIC TO OUR DB VIA THE MODEL
        data = {
            "name": request.form["name"],
            "discovery_date": request.form["discovery_date"],
            "description": request.form["description"],
            "user_id": session["user_id"], #when your adding a relic you need id of the user but if your editing you need id of the relic
        }
        relic.Relic.add_relic(data)
        return redirect("/dashboard")
        #REDIRECT TO A NEW ROUTE
        pass

@app.route("/relics/<int:id>/edit_relic_in_db", methods=["POST"])
def edit_relic_in_db(id):
    #check to see if someone is not logged in if not send to the login page
    if "user_id" not in session:
        return redirect("/")
    # validate first
    if not relic.Relic.validate_relic(request.form): #if relic fails where are we redirecting
        return redirect(f"/relics/{id}/edit") #always redirect back to previous route 
    else:
        #now we need a new class method for this
        data = {
            "name": request.form["name"],
            "discovery_date": request.form["discovery_date"],
            "description": request.form["description"],
            "id": id #id of the relic not user
        }
        relic.Relic.edit_relic(data)
        return redirect("/dashboard")
        #REDIRECT TO A NEW ROUTE
        pass



