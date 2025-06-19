# Library Management System

#In this system, there are totally four features such as:

# 1. Viewing Books
# 2. Find Book
# 3. Add Book
# 4. Delete Book
# 5. Exit
def view_books():
    # print(f"Book Id  Name \t \t Author \t Pages" )
    print(f"{'Book ID':<20}{'Title ':<15}{'Author':<15}{'Pages':<10}")
    for book in books:
        print(f"{book['id']:<20}{book['Title']:<15}{book['Author']:<15}{book['Pages']:<10}")

def find_books():
    book_id = input("Enter book id : ").strip()
    for book in books:
        if book['id'] == book_id:
            print(f"Book ID : {book['id']}")
            print(f"Title : {book['Title']}")
            print(f"Author : {book['Author']}")
            print(f"Pages : {book['Pages']}")
            return
    print('This book does not exist in the library')

def add_books():
       global book_counter
       new_id = f"Book{book_counter}"
       book_counter += 1
       title = input("Enter book title : ")
       author = input("Enter book author : ")
       pages  = input("Enter book pages : ")
       new_book = {
            'id': new_id,
            'Title':title ,
            'Author':author ,
            'Pages' : pages
        }
       books.append(new_book)
       print('\nBook added successfully')
       
       

def delete_books():
    removed = False
    view_books()
    book_id = input("Enter Book id : ").strip()
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            print('Book removed successfully')
            return
    print('This book does not exist in the library!')
   

options = {
    1:view_books,
    2:find_books,
    3:add_books,
    4:delete_books
}
def main():
    #welcome
    print("====================")
    print("Welcome to our library management system")
    print("1. Viewing Books")
    print("2. Find Book")
    print("3. Add Book")
    print("4. Delete Book")
    print("5. Exit ")
    print("====================")


    while True:
        opt = int(input('\n=> Which operation do u wanna do (1---5)?:'))
        if 1<= opt <=5:
            if opt == 5:
                print('Thanks for using our Library Management System')
                break
            options[opt]()
        else:
            print('Invalid Operation. Please enter number between 1 and 5')
        

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
book_counter = len(books) + 1
main()



