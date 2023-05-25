#!/usr/bin/env python3

class Book:

    def __init__(self, title, page_count = 0): #init method
        self.title = title #instance attribute
        self._page_count = page_count
    pass

    def get_author(self):
        return self._author #get instance property

    def set_author(self, author):
        self._author = author #set instance property

    author = property(get_author, set_author) #compiling the getter / setter 


    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        #option 1
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

        #option 2 
        # if type(page_count) == int:
        #     self._page_count = page_count
    
    page_count = property(get_page_count, set_page_count)


    def get_genre(self):
        return self._genre
    
    def set_genre(self, genre):
        self._genre = genre

    genre = property(get_genre, set_genre)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")



art_of_war = Book("The Art Of War")
print(art_of_war)
#art_of_war.set_author("Sun Tzu")
art_of_war.author = "Sun Tzu"
print(art_of_war.author)
art_of_war.set_page_count(260)
print(art_of_war.page_count)
print(art_of_war.turn_page())