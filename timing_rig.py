# intending this to be a rig to hold a python script to run timing on other programs.
# flags:
# -r <n>: run the given program(s) n times. defaults to 1 if not used, 5 for -r with no value
import os, sys

print "welcome to timing rig v0.1"
runs = 1
arglist = sys.argv
del arglist[0]

path = arglist[-1]
if not ".java" in path:
    print "cats"
else:
    os.system("javac "+path)

