# Library Management System

#In this system, there are totally four features such as:

# 1. Viewing Books
# 2. Find Book
# 3. Add Book
# 4. Delete Book
# 5. Exit
def view_books():
    print(f"Book Id  Name \t \t Author \t Pages" )
    for book in books:
        print(f"{book['id']} \t {book['Title']} \t {book['Author']} \t {book['Pages']}")

def find_books():
    book_name = input("Enter book name : ")
    for book in books:
        if book == book_name:
            print(f"{book_name} was found at index {books.index(book_name)}")
            found = True
            break
    if not found:
            print("This book doesn't exist")

def add_books():
        new_book = input("Add book : ")
        books.append(new_book)
        print("Added book successfully")

def delete_books():
    for index,book in enumerate(books):
        print(f"{index + 1} : {book}")
        index = int(input("Enter book index: ")) - 1
        books.pop(index)
        print("Book deleted successful")
books = [
    {'id': 'Book 1',
     'Title': 'Python Book',
     'Author': 'Kyaw Kyaw',
     'Pages' : 222
     },
     {'id': 'Book 2',
     'Title': 'Java Book',
     'Author': 'Aung Aung',
     'Pages' : 250
     },
     {'id': 'Book 3',
     'Title': 'Jango Book',
     'Author': 'Phyo Phyo',
     'Pages' : 232
     }
]
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

