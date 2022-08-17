class Animal:
    alive = True

    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("this rabbit is running")

class Fish(Animal):
    def swim(self):
        print("this fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("this hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.eat()
hawk.sleep()