from sys import argv

script, filename = argv

openedFile = open(filename)
print(openedFile.read())
openedFile.close()
