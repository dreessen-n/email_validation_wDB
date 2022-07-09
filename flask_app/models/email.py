# Import mysqlconnection config
from flask_app.config.mysqlconnection import connectToMySQL
import re # The regex module

"""
Import other models files for access to classes.
We import the file rather than the class to avoid circular import
Example: from flask_app.models import ninja 
"""

# Regular expression for email validation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self.data):
        """Model email"""
        self.id = data['id'],
        self.email = data['email'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']

    @classmethod
    def create_email(data):
        """Add email to db based on info passed from form"""
        query = "SELECT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL('email_val_with_db').query_db(query, data)

    @classmethod
    def display_emails(cls):
        """Show all the emails in db"""
        query = "SELECT * FROM emails;"
        emails_from_db = connectToMySQL('email_val_with_db').query_db(query)
        emails = []
        for em in emails_from_db:
            emails.append(cls(em))
        return emails

    @staticmethod
    def validate_email(email):
        """Validate that the email is in proper form and exist"""
        is_valid = True
        # Test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']):
            flash("Email is not valid!", "error")
            is_valid = False
        return is_valid


# TODO Create classmethod to interact with db: CRUD methods

