# 1. Variables
a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333333333333335 / symbol returns float by default
print(a // b)  # 3 When you use // it returns int value
print(a % b)  # 1
print(a > b)  # true
print(a < b)   # false
print(a <= b)  # false
print(a >= b)  # true
print(a == b)  # false

# loops
# for i in range(b, a):
#     print(i)

message = "Hi, Aminux How are you doing"
print(message[4:10])
print(message[-20:-5])

# A program for a party
# print("Hi, Welcome to our party, you can enjoy if you're older than 15 years")
# name = input("What is your Name: ")
# age = int(input(name + ", How Old are you "))
# limitAge = 15
# if age >= limitAge:
#     print(name + " Welcome to our party!")
#     print("What would you like to do?")
# else:
#     print("Sorry "+name+" Only adults are allowed")

# String formatting
age = 27
# print("I'm ", age, "years old")
# print("I'm "+ str(age) + " Years old")
# print("my age is {0} years old".format(age))
# # Replacement Field
# print("There are {0} days in {1}, {2}, {3}, {4}, {5} and {6} "
#       .format(31, "January", "March", "May", "July", "September", "December")) # This is called replacement field

# Display months
# print("""January is {2} days
#          February is {0} days
#          March is {2} days
#          April is {1} days
#          May is {2} days
#          June is {2} days
#          July is {2} days
#          August is {2} days
#          September is {1} days
#          October is {2} days
#          November is {1} days
#          December is {2} days
#          """.format(28, 30, 31))
# for i in range(1, 12):
#     print("No. %2d squared is %4d and cubed is 4%d" % (i, i**2, i**3))
for i in range(0, 20):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))


def main(x, y):
    return x * y
