# Import Flask app object from project folder (For python this means from the __init__.py file)
from project import app

# Import functions from flask package
from flask import render_template, redirect, url_for

# Randomize choices
from random import choice

# Create new route at '/'
@app.route('/')
def home():
    return render_template('home.html')


beginings = []
middles1 = ["The boys went out for a cold beer.", "Then, the family went to disneyland", "Everyone got hungry and ate their favorite candy bars, which was M&Ms.", ""]
middles2 = ["This was the biggest mistake the people in the previous setence ever made.", "The underaged children snuck into the club from the back.", "The dwares started to grow wings."]
ends = []

@app.route('/story/<int:part>')
def story(part):
    return render_template('home.html')