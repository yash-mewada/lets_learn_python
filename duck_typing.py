class Duck:
    def walk(self):
        print("this duck is walking")
    def talk(self):
        print("this duck is quacking")

class Chicken:
    def walk(self):
        print("this chicken is walking")
    def talk(self):
        print("this chicken is clucking")

class Person():
    def catch(self,duck):
        duck.talk()
        duck.walk()

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)