from flask import render_template
from app import app
from .request import get_books



#views
@app.route('/')
def index():
    '''
    views root page function that returns the index nd its data
    '''
    #getting books
    book_items=get_books('volumes')
     

    title='Home - Welcome to the best Book review Website Online'
    return render_template('index.html', title=title, book_items=book)



@app.route('/book/<int:book_id>')
def book(book_id):
    '''
    views books page function and returns books details page and data
    '''
    return render_template('book.html',id=book_id)
