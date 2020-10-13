from datetime import *

class Project:
    def __init__(self,n,startdate,endate):
        self.name = n
        self.startdate = startdate
        self.enddate = endate
        self.tasks = []

    def addTask(self,task):
        self.tasks.append(task)

class Task:
    def def__init__(self,name,duration):
        self.name = name
        self.duration = duration
        self.resources = []

    def addResource(self,resource):
        self.resources.append(resource)

class Resource:
    def __init__(self,n,skill):
        self.name = n
        self.skill = skill

project = Project("AI",date(2020,1,1),date(2020,2,2))
task = Task("Creating First",90)
resource = Resource("john","Python")
task.addResource(resource)
project.addTask(task)

for eachtask in project.tasks:
    print(eachtask)
    for eachresource in eachtask:
        print(eachresource.name)
        print(eachresource.skill)        