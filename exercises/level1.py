import math
"""Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints In case of input data being supplied to the question, 
it should be assumed to be a console input. tuple() 
method can convert list to tuple"""

# Solution
# x = input("Enter Numbers Seperated by (,): ")
x = '3'


def listAndTupleGen(x):
    l = x.split(",")
    t = tuple(l)
    return l, t


listAndTupleGen(x)
# values = raw_input()
# l = values.split(",")
# t = tuple(l)
# print l
# print t

''' Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters '''


# Solution


class Capitalize:
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input("Type something here: ")

    def printString(self):
        return self.s.upper()


conv = Capitalize()


''' Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. '''


# solution
# c = 50
# h = 30
# value = []
# items = [x for x in input("Enter a sequence of numbers: ").split(",")]


# # Sqrt function
# def sqrCalc():
#     # result = 0
#     for d in items:
#         result = value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
#     return result


# # print(sqrCalc())


# c = 50
# h = 30
# value = []
# items = [x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

# print(','.join(value))

''' Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

'''
# Solution
# input_str = input()
# dimensions = [int(x) for x in input_str.split(',')]
# rowNum = dimensions[0]
# colNum = dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col] = row*col

# print(multilist)

'''Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''
acceptValue = [x for x in input("Write (,) seperated words: ").split(",")]
acceptValue.sort()

print(','.join(acceptValue))

# Instruction
'''Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data '''

# Solution
# Normal way
# words = input("Write Something: ")
# words = words.split()
# removed = list(set(words))
# removed.sort()
# print(' '.join(removed))
# better Way
# words = input("Write something: ").split()
# w = list(set(words))  # Remove duplicates
# w.sort()  # sorted out
# print(' '.join(w))


# the best way
words = input("Write something: ").split()
print(" ".join(sorted(list(set(words)))))
