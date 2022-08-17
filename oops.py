from car_oops import car
car_1 = car("chevy","corvette","2021","blue")
car_2 = car("tata","tigor","2021","red")

print(car_2.model)
print(car_1.make)
print(car_2.year)
print(car_1.color)

car_2.drive()
car_1.stop()