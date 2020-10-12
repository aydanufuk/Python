f = open("files/writeIncremented.txt","w")

print("please enter text (type # when you are done)")

s=" "
while s != "#":
    s = input("enter text: ")
    f.write(s + "\n")

f.close()