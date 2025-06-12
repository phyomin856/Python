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
    found = False
    book_id = input("Enter book id : ")
    for book in books:
        if book['id'] == book_id:
            print(f"Book ID : {book['id']}")
            print(f"Title : {book['Title']}")
            print(f"Author : {book['Author']}")
            print(f"Pages : {book['Pages']}")
            found = True
            break
    if not found:
            print("This book doesn't exist")

def add_books():
       last_book = books[-1]
       last_book_id = last_book['id']
       prefix_text = last_book_id[0:4]
       real_id = int(last_book_id[4:])
       actual_id = real_id + 1
       id = prefix_text + str(actual_id)
       title = input("Enter book title : ")
       author = input("Enter book author : ")
       pages  = input("Enter book pages : ")
       new_book = {
            'id': id,
            'Title':title ,
            'Author':author ,
            'Pages' : pages
        }
       books.append(new_book)
       
       

def delete_books():
    removed = False
    view_books()
    id = input("Enter Book id : ")
    for i in range(len(books)):
        if id == books[i]['id']:
            books.pop(i)
            removed = True
            break

    if removed == True:
        print("Book removed successful")
    else:
        print("Something's wrong!")


books = [
    {'id': 'Book1',
     'Title': 'Python Book',
     'Author': 'Kyaw Kyaw',
     'Pages' : 222
     },
     {'id': 'Book2',
     'Title': 'Java Book',
     'Author': 'Aung Aung',
     'Pages' : 250
     },
     {'id': 'Book3',
     'Title': 'Jango Book',
     'Author': 'Phyo Phyo',
     'Pages' : 232
     }
]
running = True

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

