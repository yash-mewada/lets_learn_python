from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive the car")
    def stop(self):
        print("this car has stopped")

class Bike(Vehicle):
    def go(self):
        print("you ride the bike")
    def stop(self):
        print("this bike has stopped")

car = Car()
bike = Bike()  

car.go()
car.stop()
bike.go()
bike.stop()