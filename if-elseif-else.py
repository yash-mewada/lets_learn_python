age = int(input("how old are you: "))

if age >= 18:
    print("you're an adult")
elif age < 0:
    print("you have'nt been born yet")
else:
    print("you're a child")