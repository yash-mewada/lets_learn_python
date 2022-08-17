try:
    with open("C:\\Users\\Clint\\Desktop\\test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")