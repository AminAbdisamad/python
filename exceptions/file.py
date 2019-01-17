import os

file = "/Users/apple/Downloads/Tool Structure.png"

if os.path.exists(file):
    print("File Found")
else:
    print("No such file as {} exists".format(file))
