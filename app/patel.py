bookList = []
    bookDict = {}
    books = queryResult['items']
    
    for book in books:
        volumeInfo = book['volumeInfo']
        bookDict['title'] = volumeInfo['title']
        
        if 'imageLinks' in volumeInfo:
            bookDict['image'] = volumeInfo['imageLinks']['thumbnail'] 
            bookDict['pageCount'] = volumeInfo.get('pageCount', 'not available')                 
            bookDict['previewLink'] = volumeInfo.get('previewLink', 'not available')
            
            if 'authors' in book['volumeInfo']:
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
            bookDict = {}           
    extractDict['bookList'] = sortByPublishedDate(bookList)
                     
    # displayCount: number of books to be displayed
    extractDict['displayCount'] = len(bookList)
    
    return extractDict



book_results=[]
    for book_item in book_list:
        
        volumeInfo=book_list[volumeInfo]
        book_results['title']=volumeInfo['title']
         if 'imageLinks' in volumeInfo: 

            book_results['title']=volumeInfo['title']
            book_results['image'] = volumeInfo['imageLinks']['thumbnail'] 
            book_results['pageCount'] = volumeInfo.get('pageCount', 'not available')                 
            book_results['previewLink'] = volumeInfo.get('previewLink', 'not available')
            
            if 'authors' in book['volumeInfo']:
               book_results['authors'] = ", ".join(volumeInfo['authors'])
            else:
                book_results['authors'] = 'Unknown'
                
            if 'publishedDate' in volumeInfo:
                book_results['publishedDate'] = volumeInfo['publishedDate'][:4]
            else:
                book_results['publishedDate'] = 'missing'
                           
            if 'description' in volumeInfo:
                description = volumeInfo['description'][:700]                     
                if len(volumeInfo['description']) <= 700:
                    book_results['description'] = description
                else:
                    book_results['description'] = description + " '...'"   
            else:
               book_results['description'] = "No description available"              
                         
            book_ist.append(book_results)
            bookDibook_resultsct = {}           
    extractDict['bookList'] = sortByPublishedDate(bookList)
                     