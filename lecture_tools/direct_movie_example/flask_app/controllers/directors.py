from flask_app import app # Import the app
from flask import render_template, redirect, session, request
# Import your models here!
from flask_app.models import director, movie

# Where we will define our routes - we'll identify them in Monday's office hour

# Have the root route redirect to "/directors" route
@app.route("/")
def index():
    return redirect("/directors")

# This route will show all the directors from our database
@app.route("/directors")
def all_directors_page():
    # Don't forget to grab data from all the directors!
    return render_template("all_directors.html", all_directors = director.Director.get_all_directors())

# This route will display the NEW director FORM (this is NOT the same as adding a director to the database)
@app.route("/directors/new")
def new_director_page():
    return render_template("add_director.html")

# Show the details about a specific director from our database
@app.route("/directors/<int:id>/view") # Path variable called "id" that holds the ID of the individual director
def view_director_page(id):
    data = {
        "id": id,
    }
    # Formerly: this_director = director.Director.grab_one_director(data)
    return render_template("view_director.html", this_director = director.Director.grab_one_director_with_all_movies(data))

# Display the edit form for this specific director
@app.route("/directors/<int:id>/edit") # Path variable called "id" that holds the ID of the individual director
def edit_director_page(id):
    data = {
        "id": id,
    }
    return render_template("edit_director.html", this_director = director.Director.grab_one_director(data))


## INVISIBLE ROUTES
# Delete a director from our database
@app.route("/directors/<int:id>/delete")
def delete_director(id):
    data = {
        "id": id, # IMPORTANT - don't forget the ID from the path variable so we know which one we're deleting
    }
    director.Director.delete_director(data)
    return redirect("/directors")

# Route to add a director to the database (POST)
@app.route("/directors/add_to_db", methods=["POST"])
def add_director_to_db():
    # WEEK 6 onwards: Validate your form data first BEFORE adding to the database

    # Talk to the model to add this director to the database
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "birthdate": request.form["birthdate"],
    }
    director.Director.add_director(data)
    # Once we're done, we need to redirect to a new route - ALWAYS redirect when you have POST routes
    return redirect("/directors")

# Route to edit a specific director in the database (POST)
@app.route("/directors/<int:id>/edit_in_db", methods=["POST"]) # IMPORTANT: We need the ID because we need to know which director we're editing
def edit_director_in_db(id):
    # Talk to the model to add this director to the database
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "birthdate": request.form["birthdate"],
        "id": id # IMPORTANT - don't forget the ID from the path variable so we know which one we're editing
    }
    director.Director.edit_director(data)
    # Once we're done, we need to redirect to a new route - ALWAYS redirect when you have POST routes
    # new_route = "/directors/" + str(id) + "/view"
    # return redirect(new_route)
    return redirect(f"/directors/{id}/view")

# Controllers will call on the models to do validations, talk to the database, then return an HTML file or a redirect