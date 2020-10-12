#open the file foe writing
f = open("files/myfileWrite.txt","w")

s = input("please enter text: ")
f.write(s)
f.close()


