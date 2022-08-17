try:
    numerator = int(input("enter a number to divide:"))
    denominator = int(input("enter a number to divide by:"))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("can't divide by zero!")
except ValueError as e:
    print(e)
    print("enter only number please!")
except Exception as e:
    print(e)
    print("something went wrong!")
else:
    print(result)
finally:
    print("this will always execute")