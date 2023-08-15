class Library:
    def __init__(self):
        self.Nobooks = 0
        self.books = []

    def addbook(self,book):
        self.books.append(book)
        self.Nobooks = len(self.books)

    def showinfo(self):
        print(f"The numebr of books in Library are {self.Nobooks}. The books are ")
        for book in self.books:
            print(book)

l1=Library()
l1.addbook("Rick dad poor dad")
l1.addbook("C language")
l1.addbook("JAVA")
l1.addbook("Python")
l1.showinfo()
