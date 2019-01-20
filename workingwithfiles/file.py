text = 'news.txt'
# Legacy
f = open(text, 'r+')  # r - read w- write r+ - readwrite
print(f.read())
f.close()


# Context Manager
with open(text, 'r') as f:
    sizeToRead = 100
    fileContent = f.read(sizeToRead)
    # Reading the file
    # for line in f:
    #     print(line, end='')
    f.seek(0)  # reset to the begining
    f.tell()  # tells which line
    # better way to read large file
    while len(fileContent) > 0:
        print(fileContent, end='')
        fileContent = f.read(sizeToRead)

# Read file,Create new file and write to it
with open(text, 'r') as readFile:
    with open(f'{text}-copy.txt', 'w') as writeFile:
        for line in readFile:
            writeFile.write(line)
