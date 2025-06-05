# Local scope ---> global
# def greet():
#     name = "Phyo Min Khant"
# greet()

# print(name)

#Global scope ----> local
# name = "Phyo Min Khant"
# def greet():
#     print(name)
# greet()

#LEGB Rules
#Local ----> Enclosed ----> Global ----> Built-in
#name = "Phyo Min Khant" #3
def greet():
   # name = "Phyo Min" #2
    def introduction():
        name = "Khant"  #1
        print(f"My name is {name}")
    introduction()
greet()