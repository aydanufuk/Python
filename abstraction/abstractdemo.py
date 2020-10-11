from abc import abstractmethod,ABC
class Bmw(ABC):

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("starting the car")

    def stop(self):
        print("stopping the car")
# not implementing states "pass"
    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(Bmw):
    def __init__(self,cruiseControlEnable,make,model,year):
        #Bmw.__init__(self,make,model,year)
        super().__init__(make,model,year)
        self.cruiseControlEnabled = cruiseControlEnable

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):
        print("button starting the car")

    def stop(self):
        print("stopping the car")

    def drive(self):
        print("three series on drive")

class FiveSeries(Bmw):
    def __init__(self,parkingAssitantEnabled,make,model,year):
        self.__init__(self,make,model,year)
        self.parkingAssistantEnabled = parkingAssistantEnabled

    def drive(self):
        print("five series on drive")

threeSeries = ThreeSeries(True,"BMW","328i","2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()


