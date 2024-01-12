class Book:
    def __init__(self, title, author=None, page_count=0, genre=None):
        self.title = title #attribute 
        self._page_count = page_count
        self._genre = genre
    pass

    @property 
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        self._author = author 

    @property
    def page_count(self):
        return self._page_count
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, genre):
        self._genre = genre

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

art_of_war = Book("The Art of War", author="Sun Tzu", page_count=80, genre="self help")
print(art_of_war.title)
art_of_war.author ="Sun Tzu"
print(art_of_war.author)
    
