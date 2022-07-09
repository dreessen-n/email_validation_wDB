# Import mysqlconnection config
from flask_app.config.mysqlconnection import connectToMySQL

"""
Import other models files for access to classes.
We import the file rather than the class to avoid circular import
Example: from flask_app.models import ninja 
"""

class Email:
    def __init__(self.data):
        """Model email"""
        self.id = data['id'],
        self.email = data['email'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']

# TODO Create classmethod to interact with db: CRUD methods
