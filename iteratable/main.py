from math import factorial
words = "I will watch the match after I take dinner".split()
# Modern
length = [len(word) for word in words]
print(length)

# Legacy
oldLength = []
for word in words:
    oldLength.append(len(word))
print(oldLength)

# Modern
try:
    f = [len(str(factorial(x))) for x in range(30)]  # using list []
    print("Unfiltered Result", f)
    s = {len(str(factorial(x))) for x in range(30)}  # using set {}
    print("filtered Result", s)
except TypeError as e:
    print(e)

# Legacy


def legacy():
    fa = []
    for x in range(30):
        fa.append(len(str(factorial(x))))
    print(fa)


legacy()
