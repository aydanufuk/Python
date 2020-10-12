import os,sys

if os.path.isfile("files/readincremented.txt"):
    f = open("files/readincremented.txt","r")
    s = f.read()
    print(s)
    f.close()
else:
    print("file does not exist")
    sys.exit()