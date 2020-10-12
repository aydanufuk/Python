class Student:
    def __init__(self,id,name,testscrore):
        self.id = id
        self.name = name
        self.testscrore = testscrore
    
    def display(self):
        print(self.id,self.name,self.testscrore)