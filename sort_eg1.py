#list
students = ["yash","rudra","mohit"]
students.sort(reverse=True)

for i in students:
    print(i)

#with iterables
students = ("yash","rudra","mohit")
sorted_students = sorted(students,reverse=True)

for i in sorted_students:
    print(i)