'''
List: 
Hetergeneous Mutable sequence  '''

seq = "show How to index in to sequence".split()
print(seq)
slice = seq[0:4]
print(slice)

print(seq)

# print the first three items in the list
seq[:3]
# print the last three elements
seq[3:]

words = seq[:]
seq.clear()
print(seq)
print(words)


# Shallow coppies
a = [[1, 2], [23, 43]]
a[1].append(5)
b = a[:]
a[0] = [12, 15]
print(a)
print(b)
print(a == b)
print(a[0][0])
c = [[-1, +1]]*5
print(c)

# Search in lists
message = "the quick fox jumped over the lazzy dog".split()
if message.index("fox"):
    print("We found it")
else:
    print("Not found")
counter = message.count("the")
print(counter)

# Removing and cleaning lists
message.remove("quick")  # Specify Name to delete
del message[0]  # Specify list index
message.clear()  # returns empty list
message.sort()  # Sorts alphabetically
message.reverse()  # reversing lists
message.insert(0, "The")  # Index position and item to insert
message.insert(1, "Lazy")  # Index position and item to insert
# message = message.extend("fox jumped over the lazy dog")
print(message)
check = ' '.join(message)  # Convert to strig
print(check)

say = "Lovee I and You never ending have".split()
# sorting
say.sort(key=len)
sayIt = ' '.join(say)
print(say)
print(sayIt)
