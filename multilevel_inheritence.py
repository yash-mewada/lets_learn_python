class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("this animal is eating")

class Dog(Animal):
    def bark(self):
        print("this dog is barking")

dog = Dog()

dog.alive
dog.eat()
dog.bark()