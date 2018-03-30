# FUNCTIONS

# Create function


def sayHello():
    print("Hello")


sayHello()


# Create function with param

def sayHi(name):
    print('Hi ', name)


sayHi('Mohamed Amin')


# setting default param


def sayHiWithName(name='Aminux'):
    print('Hi ', name)


sayHiWithName()


# function that returns value

def add(num1, num2):
    total = num1 + num2
    return total


numSum = add(10, 34)
print(numSum)


def addOneToNum(num):
    num = num + 1
    print('Value inside function', num)
    return


num = 5
addOneToNum(num)
print('value outside the function is ', num)


def addOneToList(mylist):
    mylist.append(4)
    print('value inside function: ', mylist)
    return



mylist = [1, 2, 3]
addOneToList(mylist)
print('values outside function: ', mylist)




