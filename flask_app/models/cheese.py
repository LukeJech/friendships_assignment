
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class Cheese:
    db = "" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Cheeses Models



    # Read Cheeses Models



    # Update Cheeses Models



    # Delete Cheeses Models