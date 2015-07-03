from sys import argv

script, filename = argv

print("We're going to erase %r" % filename)
print("To kill the process, CTRL + C.")
print("To confirm, RETURN.")

input("?")

print("Opening file.")
target = open(filename, "w")

print("The file is being truncated.")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("The three lines will be written to the file.")

target.write("%r\n%r\n%r"  %(line1, line2, line3))


print("Writing is done.  Time to close the file.")
target.close()
