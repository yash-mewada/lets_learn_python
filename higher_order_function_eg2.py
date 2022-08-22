def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))