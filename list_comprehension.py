squares = [i * i for i in range(1,11)]
print(squares)

students = [100,40,60,70,50,0]
#passed_students = [i for i in students if i >=60]
passed_students = [i if i >=60 else "failed" for i in students]
print(passed_students)