from sys import argv

script, filename = argv

txt = open(filename)

print("The file is as follows: %r" % filename)
print(open(filename).read())
print(txt.read())
txt.close()

print("Type the file name again.")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
