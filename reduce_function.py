import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y:x+y,letters)
print(word)

factorial = [5,4,3,2,1]
fact = functools.reduce(lambda x,y:x*y,factorial)
print(fact)