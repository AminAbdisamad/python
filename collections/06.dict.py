'''Dict:
Unordered Mapping from unique, immutable keys to mutable values '''
# Create url dictionary
urls = {'Asal Solutions': 'www.asalsolutions.com',
        'Loopysec': 'www.loopysec.com',
        'Asal Academy': 'www.asalacademy.com',
        'SomNOG': 'www.somnog.so'}
# Another way is to use Dict
phonetix = dict(a='Alpha', b='Bravo', c="Charlee")
print(urls)
print(phonetix)

# Create tupple
namesAndAges = (('Ahmed', 29), ('Ali', 30), ('Hussein', 25))
print(namesAndAges)
# Change tupple to dict
nameAndAge = dict(namesAndAges)
print(nameAndAge)

''' Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input. '''
value = []
# numbers = [1000, 3001]
for i in range(1000, 3001):
    if i % 2 == 0:
        value = +i
print(",".join(value))
