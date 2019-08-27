
## Scrape GoodReads

#### Import Libraries


```python
# Import the Libraries
import pickle
import requests
import csv
from bs4 import BeautifulSoup as bs
import urllib
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import collections
```

#### Function for scarping goodreads


```python
# Create a function for scraping goodreads and create a csv file with the data
def scrape_goodreads(keyword):
    """ A function to scrape books data from goodreads for the genre passed as a parameter"""

    page = requests.get("https://www.goodreads.com/shelf/show/" + keyword)
    soup = bs(page.content, 'html.parser')
    titles = soup.find_all('a', class_='bookTitle')
    authors = soup.find_all('a', class_='authorName')
    books_save = 0
    books = []
    # iterate over the loop of book titles passed for the keyword parameter
    for title, author in zip(titles, authors):
        try:
            #print ("Fetching details for",title.get_text())
            url="http://www.goodreads.com/book/title.xml?key=qHWIxGrGmfBV1GhCahIHMQ&title=" + title.get_text()
            url = url.replace(' ', '%20')
            tree = ET.ElementTree(file=urllib.request.urlopen(url))
            root = tree.getroot()
            root.tag, root.attrib
            id   = root[1][0].text
            book_description = root[1][16].text
            avg_rt = root[1][18].text
            isbn = root[1][2].text
            asin = root[1][3].text
            kindle_asin = root[1][4].text
            print("book id: ",id)
            print("book title: ",title.get_text())
            print("average rating: ",avg_rt)
            #print("book description: ",book_description)
    
            # Set a counter to check how many books are being iterated
            books_save += 1
        except OSError as exc:
            if exc.errno == 36:
                print(exc)
    print("%d %s books found." % (books_save, keyword)) # books count feedback
```

#### Pass a Keyword and start seaching for books for that keyword


```python
while True:
    keyword = input("Enter the search string (or quit to stop): ").lower()
    if(keyword == "quit"):
        break
    else:
        scrape_goodreads(keyword)
```

    Enter the search string (or quit to stop): fiction
    book id:  18922692
    book title:  1984 (Kindle Edition)
    average rating:  4.12
    book id:  4671
    book title:  The Great Gatsby (Paperback)
    average rating:  3.91
    book id:  3
    book title:  Harry Potter and the Sorcerer's Stone (Harry Potter, #1)
    average rating:  4.46
    book id:  360395
    book title:  The Catcher in the Rye (Paperback)
    average rating:  3.64
    book id:  2767052
    book title:  The Hunger Games (The Hunger Games, #1)
    average rating:  4.33
    book id:  968
    book title:  The Da Vinci Code (Robert Langdon, #2)
    average rating:  3.82
    book id:  35354014
    book title:  The Handmaid's Tale (Paperback)
    average rating:  3.21
    book id:  5907
    book title:  The Hobbit or There and Back Again (Paperback)
    average rating:  4.26
    book id:  1885
    book title:  Pride and Prejudice (Paperback)
    average rating:  4.25
    book id:  15881
    book title:  Harry Potter and the Chamber of Secrets (Harry Potter, #2)
    average rating:  4.41
    book id:  5
    book title:  Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)
    average rating:  4.55
    book id:  38226643
    book title:  The Alchemist (Paperback)
    average rating:  3.79
    book id:  6
    book title:  Harry Potter and the Goblet of Fire (Harry Potter, #4)
    average rating:  4.55
    book id:  15167659
    book title:  Life of Pi (Paperback)
    average rating:  4.25
    book id:  6148028
    book title:  Catching Fire (The Hunger Games, #2)
    average rating:  4.29
    book id:  2429135
    book title:  The Girl with the Dragon Tattoo (Millennium, #1)
    average rating:  4.13
    book id:  136251
    book title:  Harry Potter and the Deathly Hallows (Harry Potter, #7)
    average rating:  4.63
    book id:  1
    book title:  Harry Potter and the Half-Blood Prince (Harry Potter, #6)
    average rating:  4.56
    book id:  2
    book title:  Harry Potter and the Order of the Phoenix (Harry Potter, #5)
    average rating:  4.49
    book id:  7260188
    book title:  Mockingjay (The Hunger Games, #3)
    average rating:  4.03
    book id:  29057333
    book title:  The Help (Hardcover)
    average rating:  4.42
    book id:  1618
    book title:  The Curious Incident of the Dog in the Night-Time (Paperback)
    average rating:  3.87
    book id:  36519911
    book title:  Slaughterhouse-Five (Paperback)
    average rating:  4.06
    book id:  22084549
    book title:  Gone Girl (Paperback)
    average rating:  4.25
    book id:  35677451
    book title:  Of Mice and Men (Paperback)
    average rating:  0.00
    book id:  960
    book title:  Angels & Demons (Robert Langdon, #1)
    average rating:  3.88
    book id:  34682293
    book title:  Jane Eyre (Paperback)
    average rating:  3.68
    book id:  42819174
    book title:  The Road (Hardcover)
    average rating:  3.95
    book id:  32879951
    book title:  The Girl on the Train (Hardcover)
    average rating:  0.00
    book id:  13496
    book title:  A Game of Thrones (A Song of Ice and Fire, #1)
    average rating:  4.45
    book id:  386162
    book title:  The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy, #1)
    average rating:  4.22
    book id:  9681098
    book title:  Catch-22 (Paperback)
    average rating:  4.19
    book id:  15800968
    book title:  The Adventures of Huckleberry Finn (Paperback)
    average rating:  3.57
    book id:  34
    book title:  The Fellowship of the Ring (The Lord of the Rings, #1)
    average rating:  4.35
    book id:  34393099
    book title:  Frankenstein (Paperback)
    average rating:  4.10
    book id:  28085
    book title:  One Hundred Years of Solitude (Hardcover)
    average rating:  4.07
    book id:  40786297
    book title:  The Picture of Dorian Gray (Paperback)
    average rating:  5.00
    book id:  36381933
    book title:  All the Light We Cannot See (Hardcover)
    average rating:  5.00
    38 fiction books found.
    Enter the search string (or quit to stop): quit



```python

```
