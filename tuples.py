student = ("bob",21,"male")
print(student.count("bob"))
print(student.index("male"))
for x in student:
    print(x)
for i in student:
    if "bob" in student:
        print("bob is here")