from flask_app import app
from flask_app.controllers import directors, movies # IMPORTANT: import ALL your contorller files!!!

if __name__=="__main__":
    app.run(debug=True)