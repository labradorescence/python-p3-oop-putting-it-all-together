#!/usr/bin/env python3

class Book:

    def __init__(self, title, page_count = 0): #init method
                            #self === instance
        self.title = title #instance attribute
        self._page_count = page_count
    pass

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author #set instance property

    author = property(get_author, set_author)

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else: 
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def get_genre(self):
        return self._genre
    
    def set_genre(self, genre):
        self._genre = genre
    
    genre = property(get_genre, set_genre)

art_of_war = Book("The Art of War")
print(art_of_war)
art_of_war.set_author("Sun Tzu")
print(art_of_war.author)

art_of_war.set_page_count(260)
print(art_of_war.page_count)

art_of_war.set_genre("Non-fiction")
print(art_of_war.genre)