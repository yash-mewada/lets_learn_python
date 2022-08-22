#with other iterables like tuples of tuples
students = (("yash","O",80),
            ("rudra","O+",85),
            ("ashish","f",39))
mark = lambda marks:marks[2]
sorted_students = sorted(students,reverse=True)

for i in sorted_students:
    print(i)