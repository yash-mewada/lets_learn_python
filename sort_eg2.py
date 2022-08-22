#with list of list of tuples
students = [("yash","O",80),
            ("rudra","O+",85),
            ("ashish","f",39)]
mark = lambda marks:marks[2]
students.sort(key=mark,reverse=True)

for i in students:
    print(i)

