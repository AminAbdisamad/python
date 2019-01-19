# import module1
# p1 = module1.Person("Hassan",34)
from module1 import Person as p
p1 = p("Idris",56)

print(p1.greeting())


# Open file and read

# Normal way 
f = open('text.txt')
text = f.read()
for line in text.split('\n'):
    pass
    # print(line)
f.close()

# better way

f = open('text.txt')
for line in f:
    pass
    # print(line)
f.close()

# best way
with open('text.txt') as f:
    text = f.read()
    for line in text.split('\n'):
        print(line)