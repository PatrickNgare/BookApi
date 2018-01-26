from app import app
import urllib.request,json
from .models import book

Book= book.Book

#getting api key

key=app.config['BOOK_API_KEY']
base_url=app.config['BOOK_API_BASE_URL']


def get_books(gifted):
    '''
    Funstion that gets the json to our url request
    '''
    get_books_url=base_url.format(volumes,key)
    with urllib.request.urlopen(get_books_url) as url:
        get_books_data=url.read()
        get_books_response=json.loads(get_books_data)
        book_results=None
    
        if get_books_response['items']:
            book_results_list=get_books_response['items']
            book_results=process_results(book_results_list)
            
        
    return book_results



def process_results(book_results):
    
    bookList=[]
    bookDict={}
    for result in book_results:
        volumeInfo=result['volumeInfo']
        bookDict['title']=volumeInfo['title']
        if 'imageLinks' in volumeInfo:
                bookDict['image'] = volumeInfo['imageLinks']['thumbnail'] 
                bookDict['pageCount'] = volumeInfo.get('pageCount', 'not available')                 
                bookDict['previewLink'] = volumeInfo.get('previewLink', 'not available')
                
                if 'authors' in result['volumeInfo']:
                    bookDict['authors'] = ", ".join(volumeInfo['authors'])
                else:
                    bookDict['authors'] = 'Unknown'
                    
                if 'publishedDate' in volumeInfo:
                    bookDict['publishedDate'] = volumeInfo['publishedDate'][:4]
                else:
                    bookDict['publishedDate'] = 'missing'
                            
                if 'description' in volumeInfo:
                    description = volumeInfo['description'][:700]                     
                    if len(volumeInfo['description']) <= 700:
                        bookDict['description'] = description
                    else:
                        bookDict['description'] = description + " '...'"   
        else:
            
            bookDict['description'] = "No description available"              
                            
            
            bookList.append(bookDict)
            
            
            # bookDict = {}           
            # extractDict['bookList'] = sortByPublishedDate(bookList)
                        
            # extractDict['displayCount'] = len(bookList)
            print(bookList)
        
    return bookList

































        

