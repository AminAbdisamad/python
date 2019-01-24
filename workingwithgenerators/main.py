# Square numbers
def squareNumbers(num):
    result = []
    for i in num:
        result.append(i*i)
    return result


# print(squareNumbers([1, 2, 3, 4, 5]))

# Generators is better for performance coz its holding all the values in the memory - it keeping one value at a time


def squaregen(num):
    for i in num:
        yield i*i


nums = squaregen([2, 3, 4, 5, 6])
for x in nums:
    print(x)
