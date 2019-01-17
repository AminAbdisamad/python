'''Range: Arithmetic progression of integer 
range(5) - stops at 5
range(1,10) - returns range between 1 and 9 
range(1,10,3) - start, stop, step
Avoid range for iterating over list
'''
a = range(5)
print(a)
b = range(4, 10)

c = list(range(12, 45, 3))
print(c)


names = ["Hassan", "Hussien", "Ahmed", "Ugaas", "Buubaa"]
# Abusing range
for i in range(len(names)):
    print(names[i])
# Better way
for i in names:
    print(i)
# with index
for i in enumerate(names):
    print(i)
# best way
for i, v in enumerate(names):
    print("Index = {0}, Value = {1}".format(i, v))
