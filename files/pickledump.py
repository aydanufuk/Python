import pickle,student

f = open("files/student.dat","wb")
s = student.Student(123,"john",90)
pickle.dump(s,f)
f.close()