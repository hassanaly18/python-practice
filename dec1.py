def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    print("hello")
    return wrapper

@decorator
def greet():
    print("Hello, World!")

greet()