# Import app
from flask_app import app

# Import modules from flask
from flask import Flask, render_template, request, redirect, session, url_for

# Import models class
from flask_app.models.email import Email

# Create the routes

@app.route('/')
def index():
    """Homepage"""
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def add_email():
    if not Email.validate_email(request.form):
        # Redirect back to form
        return redirect('/')
    # Create data dict based on request.form
    # The keys must match exactly to the variables in query str
    data = {
        'email': request.form['email'],
}
    # Pass the data dict to create_email method in class
    Email.create_email(data)
    # Redirect to display page
    return redirect('/success')

@app.route('/success')
def display_all():
    """Display all the emails in db"""
    all_emails = Email.display_emails()
    return render_template('success.html', all_emails= all_emails)


# TODO set routes to READ - SELECT from db in models

# TODO set routes to UPDATE - UPDATE from db in models

# TODO set routes to DELETE - DELETE from db in models
@app.route('/delete_email', methods=['POST'])
def remove_email():
    """Remove email from db"""
    data = {
        'email_id': request.form['email_id']
    }
    Email.delete_email(data)
    return redirect('/success')


