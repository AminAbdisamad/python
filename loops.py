# For Loops

People = ['Amin', 'Abdihalim', 'Ali', 'Hassan']
for person in People:
    print('Current Person: ', person)

# Iterative by sequence
for i in range(len(People)):
    print(People[i])

# for i in range(0, 10):
#     print(i)

# While Loops
count = 0
while count <= 20:
    print(count)
    count +=1

# Breaking While Loops
count = 0
while count <= 20:
    if count == 10:
        break
    print(count)
    count = count + 1