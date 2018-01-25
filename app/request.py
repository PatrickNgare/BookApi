from app import app
import urllib.request,json
from .models import book

Book= book.Book

#getting api key

api_key=app.config['BOOK_API_KEY']
base_url=app.config['BOOK_API_BASE_URL']


def get_books(volumes):
    '''
    Funstion that gets the json to our url request
    '''
    get_books_url=base_url.format(volumes,api_key)
    with urllib.request.urlopen(get_books_url) as url:
        get_books_data=url.read()
        get_books_response=json.loads(get_books_data)
        print(get_books_response)
        book_results=None
        if get_books_response['items']:
            book_results_list=get_books_response['items']
            book_results=process_results(book_results_list)
            
        
    return book_results



def process_results(book_list):
    

    book_results=[]
    for book_item in book_list:
        id=book_item.get('id')
        print(id)
        description=book_item.get('description')
        print(description)
        title = book_item.get('volumeInfo')['title']
        print(title)
        authors = book_item.get('volumeInfo')['subtitle']
        print(authors)
        # # thumbnail=book_item.get('imageLinks')['thumbnail']
        # print(thumbnail)
        # if thumbnail:
        #     book_object=Book(id,description, authors, title)
        #     book_results.append(book_object)
    return book_results        
       
































        

