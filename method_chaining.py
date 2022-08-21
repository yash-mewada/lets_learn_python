class Car:
    def turn_on(self):
        print("you start the engine")
        return self

    def drive(self):
        print("you are driving")
        return self

    def brake(self):
        print("you hit thr brakes")
        return self

    def turn_off(self):
        print("you turn off the engine")
        return self

car = Car()
car.turn_on().drive().brake().turn_off()