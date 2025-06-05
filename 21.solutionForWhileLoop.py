# user put number ->start count -> number->sort -> until >=0
# num = int(input("Put a number : "))
# if num < 0:
#     print("Invalid number")
# else:
#     print("Starting CountDown")
# while num > 0:
#     print(num)
#     num -= 1
# print("Finish CountDown : ")


# import random
# ran_num = random.randint(1,20)
# print(ran_num)
# guess = None
# attempt = 0
# while guess != ran_num:
#     guess = int(input("Your guess number : "))
#     attempt += 1
#     if guess < ran_num:
#         print("Your Guess number is too low")
#     elif guess > ran_num:
#         print("Your Guess number is too high")
#     else:
#         print("Congratulation ! You won Guessing number game !")
#         print(f"You won the game in {attempt} attempt. ")

import random
rum_num = random.randint(1,22)
print(rum_num)
guess = None
attempt = 0
while guess != rum_num:
    guess = int(input("Your gess number : "))
    attempt += 1

    if guess < rum_num:
        print("Your guess number is too low")
    elif guess > rum_num:
        print("Your guess number is too high")
    else:
        print("Contradulation")
        print(f"You won the game in {attempt} attempt")
