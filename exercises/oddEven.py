'''A program that tells whether a number is even or odd '''

number = 90


# Tells wether number is even or odd
def oddEven(number):
    if number % 2 == 0:
        return("{0} is even Number".format(number))
    else:
        return("{0} is odd Number".format(number))


# function call
oddEven(number)


# Generate a new list from the user input
def displayaListOfLessNumbers():
    user = int(input("Enter a number: "))
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for i in a:
        if i <= user:
            b.append(i)
    return(b)


# function call
# displayaListOfLessNumbers()

# Print out numbers they're in same
def commonNumbers():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    value = []
    for i in a:
        if i in b:
            value.append(i)
    return(list(set(value)))
