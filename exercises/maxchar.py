#  Given string find the maximum characters


def maxChars(ss):
    # Create a new dictonary that holds the char and repeated number
    # map = {}
    # for letter in word:
    #     if(map[letter]):
    #         map[letter] = map[letter]+1
    #     else:
    #         map[letter] = 1
    # return map[letter]
    return max(ss, key=ss.count)


print(maxChars("Hello There!"))

# map = {'id':1,'name':'Hassan','Address':'Serdivan'}

# for  letter in map:
#     print('{}: {}'.format(letter,map[letter]))

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# # thisdict["year"] = 2018
# car.update({'year': 2018, 'price': '$500B'})
# car['logo'] = 'Somthing'

# print(car)
