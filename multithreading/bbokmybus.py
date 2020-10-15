from threading import *

class BookMyBus:

    def __init__(self,availableSeats):
        self.availableSeats = availableSeats
        self.l = Lock()

    def buy(self,seatsRequired):
        self.l.acquire()
        print("total seats available ",self.availableSeats)

        if(self.availableSeats >= seatsRequired):
            print("confirming a seat")
            print("processing the payment")
            print("printing the ticket")
            self.availableSeats -= seatsRequired
        else:
            print("sorry no seats available")
        self.l.release()

obj = BookMyBus(10)
t1 = Thread(target=obj.buy,args=(3,))
t2 = Thread(target=obj.buy,args=(4,))
t3 = Thread(target=obj.buy,args=(4,))

t1.start()
t2.start()
t3.start()