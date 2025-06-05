#while loop
# num = 10
# loop = 1
# while loop <= num:
#     print("Hello World")
#     loop += 1

valid_num = False
while not valid_num:
    age = input("Enter your age : ")
    if age.isdigit() and int(age):
        valid_num = True
    else:
        print("Invalid age : enter the valid one")
