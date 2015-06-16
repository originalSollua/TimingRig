# intending this to be a rig to hold a python script to run timing on other programs.
# flags:
import os, sys, time

print "welcome to timing rig v0.1"
arglist = sys.argv
del arglist[0]

path = arglist[-1]
if not ".java" in path:
    sys.exit("No .java file specified")
else:
    var = os.system("javac "+path)
    if not var == 0:
        sys.exit("Invalid path to program")
    print path
    path = path[:-5]
    print path
    t = time.clock()
    var = os.system("java "+path)
    e = time.clock()
    if not var == 0:
        sys.exit(path +" could not be run.")
    print "Elapsd Execution time: "+str(e - t)+" Sec"
    sys.exit(0)
       

