''' 
Tupple : heterogeneous immutable sequence.
It can't be replaced or removed and new elements cannot be added
'''
cities = ("Mogadishu", "Istanbul", "London", "Tokiyo", "Doha")
multipleFive = cities * 5
print(cities[0])
# Add a new city
# cities + ("Newyork")
# find length of cites
len(cities)

# Nested tuples
locationMap = ((45.084, 25.236), (4537, 57685), (347.93, 45784))
print(locationMap[2][0])

# Creating single tuple
single = ('57',)
print(type(single))

# Creating Empty tuple

empty = ()

4 in (34, 35, 65, 67)  # returns false
5 in (43, 232, 54, 4, 3, 5)  # returns true

# a function that returns min and max of items


def minMax(items):
    return min(items), max(items)


if __name__ == '__main__':
    print(minMax([12, 3, 4, 56, 67, 878, 89, 0]))
    lowest, highest = minMax([12, 43, 45, 565, 768, 0])
    print(highest, lowest)
