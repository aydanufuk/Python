import pickle

f = open("files/student.dat","rb")

obj = pickle.load(f)

obj.display()

f.close()