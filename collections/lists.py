# Lists

pl = ["C","C++","Java","Go","Python"]
# Swap Python to C 
temp = pl[0]
pl[0] = pl[4]
pl[4] = temp
# print(pl)

# Dictionary
userInfo = {
    "Name":"Gorad",
    "age":20,
    "Study": True,
    "Work": False,
    "Email":"gorad@gmail.com"
}



# Classes
class Employee:
  
    def __init__(self,name,age,email):
        self._name = name
        self._age = age
        self._email = email
    def greeting(self):
        print("Hello, My Name is {}, I'm {} years old. contact me at {} ".format(self._name,self._age,self._email))



person1 = Employee(userInfo["Name"],userInfo["age"],userInfo["Email"])
# person1.name = userInfo["Name"]
# person1.age = userInfo["age"]
# person1.email = userInfo["Email"]
person1.greeting()


''' Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320''' 
# number = int(input("Enter a number: "))

def fact(number):
    if number == 0:
        return 1
    return number * fact(number - 1)

# x=int(raw_input())
# print(fact(number))

'''With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict() '''

# # n = int(input("Enter a Number"))
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i


a = [1,2,4,8,16,32,64]
#  Comprehensive list
b = [ i*2 for i in a]

print(a)
print(b)




