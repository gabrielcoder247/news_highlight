from flask import render_template
from app import app
#view
@app.route('/')
def index():
    '''
    view root function that returns the index page and it's data
    '''
    title = 'Home - Welcome to the best News- Highlight website Online'

    return render_template('index.html',title=title)
