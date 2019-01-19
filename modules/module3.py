test = "This is a test"


def findIndex(searchList, target):
    """This function returns the index of searched Item"""
    for i, value in enumerate(searchList):
        if value == target:
            return i
    return -1
