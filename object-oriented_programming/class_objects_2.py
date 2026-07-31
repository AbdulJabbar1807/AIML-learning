class Book: # class
    def __init__(self,id,title,author) -> None: # constructor
        # self - its a parameter in python that refers to current object,with it python automatically passes object as the first argument when an instance method is called.
        self.id = id    # -> atomic.id = id        #instance variable or Attribute
        self.title = title      #instance variable or Attribute
        self.author = author.upper()    # instance variable or Attribute
        
    def display(self):   # -> display(atomic)   # Method-functions it can perform.
        print(f"Id: {self.id}") # -> atomic.id
        print(f"Title: {self.title}") # -> atomic.title
        print(f"Author: {self.author}") # -> atomic.author
        
atomic = Book(102,"Atomic Habits","James clear") # object or instance
atomic.display()
