from flask import render_template
from app import app



#views
@app.route('/')
def index():
    '''
    views root page function that returns the index nd its data
    '''
    return render_template('index.html')