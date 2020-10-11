from abc import abstractmethod,ABC
class Bmw(ABC):

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
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
        super().start()
        print("button starting the car")

    def stop(self):
        super().stop()
        print("stopping the car")

    def drive(self):
        print("three series on drive")

class FiveSeries(Bmw):
    def __init__(self,parkingAssitantEnabled,make,model,year):
        self.__init__(self,make,model,year)
        self.parkingAssistantEnabled = parkingAssistantEnabled

    def drive(self):        
        print("five series on drive")

    def start(self):
        super().start()
        print("button starting the car")

    def stop(self):
        super().stop()
        print("stopping the car")

threeSeries = ThreeSeries(True,"BMW","328i","2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()


