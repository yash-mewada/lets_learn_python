def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("hello")
    print(text)

hello(loud)
hello(quiet)