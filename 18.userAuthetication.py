# name = input("Your name : ")
# age = input("Your age : ")
# print(f"Your name is {name} and age is {age}")

#
# num_1 = input("number 1 is : ")
# chg_int_1 = int(num_1)
# num_2 = input("num 2 is : ")
# chg_int_2 = int(num_2)
# result = chg_int_1 + chg_int_2
# print(f"Result : {result} ")

# num_1 = int(input("number 1 is : "))
# num_2 = int(input("number 2 is : "))
# result = num_1 + num_2
# print(f"Total number is : {result}")

# User Authentication System
user_name = "phyominkhant106@gmail.com"
pass_word = 12345

print("You need to first login. If successful you can use it")
username = input("Username : ")
password = int(input("Password : "))
if username == user_name and password ==pass_word:
    print("Login successful")
else:
    print("Try again")