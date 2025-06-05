# Library Management System

#In this system, there are totally four features such as:

# 1. Viewing Books
# 2. Find Book
# 3. Add Book
# 4. Delete Book
# 5. Exit
def view_books():
    for index,book in enumerate(books):
        print(f"{index + 1} : {book}")

def find_books():
    book_name = input("Enter book name : ")
    for book in books:
        if book_name == book:
            print(f"{book_name} was found at index {books.index(book_name)}")
            found = True
            break
        if not found:
            print("This book doesn't exist")

def add_books():
        add_book = input("Add book : ")
        books.append(add_book)
        print("Added book successfully")

def delete_books():
    for index,book in enumerate(books):
        print(f"{index + 1} : {book}")
        index = int(input("Enter book index: ")) - 1
        books.pop(index)
        print("Book deleted successful")
books = ['The Lion King','Python Programming','The lost of the Ring','Harry Potter','Kingdom']
running = True
found = False
#welcome
print("====================")
print("Welcome to our library management system")
print("1. Viewing Books")
print("2. Find Book")
print("3. Add Book")
print("4. Delete Book")
print("5. Exit ")
print("====================")


while running:
    opt = int(input('\n=> Which operation do u wanna do (1---5)?:'))
    if opt == 1:
        view_books()
    elif opt == 2:
        find_books()
    elif opt == 3:
       add_books()
    elif opt == 4:
        delete_books()
    elif opt == 5:
        running = False
        print("Thanks for using our Library Managemnent System")
    
    else:
        print("Invaid")

