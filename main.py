""" A python program that prints texts to the console"""
# def readFile():
#     f = open("data.txt", "r")
#     text = f.read()
#     for line in text.split('\n'):
#         print(line)

#     f.close()


# readFile()

def readFile2():
    """ ReadFile2 is function that reads a given file and outputs to the console

        Args: an iteratable list of text
     """
    with open('data.txt') as data:
        for text in data:
            print(text)


m = [22, "45", "Google", "IOS"]


# Modify function
def modifier(k):
    # Before Modified
    print("M = {}".format(m))
    k.append("Apple")
    k.append("Facebook")
   # After Modified
    print("K = {}".format(k))


# Banner Function
def banner(message, border="_"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


# Create list of menu
breakfast = ["Egg", "Sausage", "Banana"]
lunch = ["Pasta", 'Bariis']


def menuList(menu=None):
    if menu is None:
        menu = []
    menu.append("Spam")
    return menu


# Calling functions
if __name__ == '__main__':
    # readFile2()
    # modifier(m)
    banner("Welcome to My program")
    print(menuList(breakfast))
