class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no está disponible")

    def return_book(self):
        self.available = True
        print(f"El libro {self.title} ha sido devuelto")


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} no está disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} no está en la lista de prestados")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido añadido") 

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_available_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"{book.title} de {book.author}")

# Crear los libros y usuarios
book1 = Book("El Principito", "Antoine de Saint-Exupéry")
book2 = Book("El Hobbit", "J.R.R. Tolkien")
book3 = Book("El Hobbit 2", "J.R.R. Tolkien")
book4 = Book("El Hobbit 3", "J.R.R. Tolkien")
user1 = User("Ana", 1)
user2 = User("Juan", 2)

# Añadir los libros y usuarios a la biblioteca
library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.register_user(user1)
library.register_user(user2)

# Mostrar los libros disponibles
library.show_available_books()

# Prestar un libro a un usuario
user1.borrow_book(book1)

# Mostrar los libros Disponibles
library.show_available_books()

# Devolver un libro a un usuario
user1.return_book(book1)

# Mostrar los libros Disponibles    
library.show_available_books()