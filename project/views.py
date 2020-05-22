# Import Flask app object from project folder (For python this means from the __init__.py file)
from project import app

# Import functions from flask package
from flask import render_template, redirect, url_for, make_response

# Randomize choices
from random import choice

# Create new route at '/'
@app.route('/')
def home():
    return render_template('home.html')


beginings = []
middles1 = []
middles2 = []
ends = []

@app.route('/story/<int:part>')
def story(part):

    if part == 0:
        story = choice(beginings)
    elif part == 1:
        story = choice(middles1)
    elif part == 2:
        story = choice(middles1)
    elif part == 3:
        story = choice(middles1)
    else:
        flash('Error no story part found', 'error')
        return redirect(url_for('home'))
    page = make_response(render_template('story.html', story=story))
    page.set_cookie(f'part{part}', f'{story}', max_age=60 * 60 * 24 * 365)