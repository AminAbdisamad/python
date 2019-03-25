from getpass import getpass

# Tip 1
condition = False
# if condition:
#     x = 1
# else:
#     x = 0
# print(x)

# Better way  using ternary operator 
x = 1 if condition else 0

# Tip 2: Working with large numbers 
number1 = 100_000
number2 = 100_000_000
total = number1 + number2
# print(f'{total:,}')

# # Tip 3: Using enumerate in lists
names = ['Hassan','Ali','Ahmed']
for index, name in enumerate(names):
    pass
    # print(index,name)

# # Tip 4: Looping through two lists
names = ['Dirie','Farah','Sheikh']
profession = ['Network Engineer','Civil Engineer','Business Development Consultant']
for index, name in enumerate(names):
    job = profession[index]
    # print(f'{name} works as a {job}')

names = ['Dirie','Farah','Sheikh']
professions = ['Network Engineer','Civil Engineer','Business Development Consultant']
for name, profession in zip(names,professions):
    pass
    # print(f'{name} works as a {profession}')

# Tip 5: Unpacking values 
a,b, *c ,d= (1,2,3,4,5,6)

# Tip 6: Setters and getters 
class Person:
    pass

person = Person()
person_info = {'first':'Aminux','last':'Abdi'}
#  I want to extract the key and value to make the property and value of a person object
for key, value in person_info.items():
    setattr(person,key,value)

person.first
person.last

# Tip 7: Getpass - hiding password
username = input("User Name: ")
password= getpass("Password: ")
print("Logging in .....")
