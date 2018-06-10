# # Number Guesser Game
# print("Hello, Welcome to Number Guesser Game ")
# print("======================================")
# name = input("What's your name, please: ")
# age = int(input("How old are you {} ".format(name)))
# # only teenagers can play the game 18 years
# if age >= 18:
#     print("You are allowed to play the game")
#     guess = int(input("I'm thinking of a number between 1 and 10 can you guess? "))
#     if guess < 5:
#         guess = int(input("Please guess higher number "))
#         if guess == 5:
#             print("Congrats, {} you're wonderful".format(name))
#         else:
#             print("sorry! you didn't get the number")
#     elif guess > 5:
#         guess = int(input("Please guess lower number "))
#         if guess == 5:
#             print("Wonderful {}, you did it".format(name))
#         else:
#             print("sorry! you didn't get it")
#     else:
#         print("Amazing genius {}, you did it on your first try".format(name))
# else:
#     print("Sorry! you are not allowed to play it right now please come back in {} years".format(18 - age))

# Refactoring code
print("Hello, Welcome to Number Guesser Game ")
name = input("What's your name, please: ")
age = int(input("How old are you, {} ".format(name)))
# only teenagers can play the game 18 years
if age >= 18:
    guess = int(input("I'm thinking of a number between 1 and 10 can you guess? "))
    if guess != 5:
        if guess < 5:
            guess = int(input("Please guess higher number "))
        else:
            guess = int(input("Please guess lower number "))
        if guess == 5:
            print("Congrats, {} you're wonderful".format(name))
        else:
            print("sorry! you didn't get the number")
    else:
        print("Amazing genius {}, you did it on your first try".format(name))
else:
    print("Sorry! you are not allowed to play it right now please come back in {} years".format(18 - age))
