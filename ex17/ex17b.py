from sys import argv
from os.path import exists

script, in_file, out_file = argv

open(out_file, "w").write(open(in_file).read())
print("%s contents written to %s contents." %(in_file, out_file))

#it works.  cool!
