# Import mysqlconnection config
from flask_app.config.mysqlconnection import connectToMySQL
import re # The regex module
from flask import flash

"""
Import other models files for access to classes.
We import the file rather than the class to avoid circular import
Example: from flask_app.models import ninja 
"""

# Regular expression for email validation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        """Model email"""
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_email(cls, data):
        """Add email to db based on info passed from form"""
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL('email_val_with_db').query_db(query, data)

    @classmethod
    def display_emails(cls):
        """Show all the emails in db"""
        query = "SELECT * FROM emails;"
        emails_from_db = connectToMySQL('email_val_with_db').query_db(query)
        all_emails = []
        for row in emails_from_db:
            all_emails.append(cls(row))
        return all_emails

    @classmethod
    def delete_email(cls, data):
        query = "DELETE FROM emails WHERE id=%(email_id)s;"
        return connectToMySQL('email_val_with_db').query_db(query,data)
        


    @staticmethod
    def validate_email(email):
        """Validate that the email is in proper form and exist"""
        is_valid = True
        # Check for if email has already been used and stored in db
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        result = connectToMySQL('email_val_with_db').query_db(query, email)
        # Check to see if the query returned an result with that email; if yes
        # return False
        if len(result) >= 1:
            flash("Email is already used. Please sign in or register with different email.", "danger")
            is_valid = False
            return is_valid
        # Test whether a field matches the pattern
        if not EMAIL_REGEX.match(email['email']):
            flash("Email is not valid!", "danger")
            is_valid = False
            return is_valid
        else:
            flash(f"The email address you entered: {email['email']} is VALID email address! Thank you!", "success")
        return is_valid


# TODO Create classmethod to interact with db: CRUD methods

