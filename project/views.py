# Import Flask app object from project folder (For python this means from the __init__.py file)
from project import app

# Import functions from flask package
from flask import render_template, redirect, url_for, make_response, request

# Randomize choices
from random import choice

# Create new route at '/'
@app.route('/')
def home():
    return render_template('home.html')

beginings = ['There was a little boy.','This person had no father and was raised by their grandparents.']
middles1 = ["The boys went out for a cold beer.", "Then, the family went to disneyland", "Everyone got hungry and ate their favorite candy bars, which was M&Ms."]
ends = ['He ate a poisoned apple and died', 'She discovered a pot of gold at the end of the rainbow', 'He fell off a cliff and died’,  ‘She became an all-powerful wizard and conquered the world’, ‘He graduated Hogwarts and defeated Lord Voldemort', 'They lived in a cave happily ever after']

@app.route('/story/<int:part>')
def story(part):

    story = ''

    if part == 0:
        story = choice(beginings)
    elif part == 1:
        story = choice(middles1)
    elif part == 2:
        story = choice(ends)
    else:
        return redirect(url_for('home'))

    page = make_response(render_template('story.html', story=story, part=part+1))
    page.set_cookie(f'part{part}', f'{story}', max_age=60 * 60 * 24 * 365)
    return page


@app.route('/story/end')
def end():

    siteCookies = request.cookies

    if 'part0' in siteCookies and 'part1' in siteCookies and 'part2' in siteCookies:

        part0 = siteCookies['part0']
        part1 = siteCookies['part1']
        part2 = siteCookies['part2']

        return render_template('end.html', part0=part0, part1=part1, part2=part2)

    else:

        return redirect(url_for('home'))