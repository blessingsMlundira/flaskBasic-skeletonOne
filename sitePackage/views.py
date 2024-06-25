from flask import Blueprint, render_template, request, flash, jsonify, request
from flask_login import login_required, current_user

from . import db

import io
import base64

import requests  # Add this line to import the requests module

# Blueprint for views
views = Blueprint('views', __name__)
views.secret_key = 'your_secret_key'  # Set a secret key for session management


# Route for the home page
@views.route('/', methods=['GET', 'POST'])
@login_required  # Requires login to access this route
def home():
    return render_template("index.html", user=current_user)

@views.route('/explore')
def explore():
    return render_template('explore.html', user=current_user)