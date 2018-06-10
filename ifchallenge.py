"""
Challenge1.
Write a small program to ask user for a name and age when both values
have been entered, check if the person is the right age between 18 and 30
(over 18 and under 30) if they are, welcome them to the holiday, otherwise print
a polite message refusing them entry
"""
name = input("What's your name: ")
age = int(input("How old are you, {}? ".format(name)))
if 18 < age < 31:
    print("Welcome to the holiday!")
else:
    print("{}, Sorry! you're not selected ths time".format(name))

