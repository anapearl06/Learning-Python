def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

greet = say_hello   
greet()  # This will call the wrapper function, which in turn calls say_hello

print(greet.__name__)  # This will print the name of the wrapper function, which is 'wrapper'