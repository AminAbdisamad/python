import os
import sys

# change Directory
os.chdir('/Users/apple/Desktop')
# to create a directory
# os.makedirs("CodeWithAmin")

if __name__ == "main":
    # To find out os methods and attributes
    # print(dir(os))
    # Current Working directory
    print(os.getcwd())

    print(os.listdir())
    print(dir(sys))
