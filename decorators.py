def decorator_func(message):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            print(message)  # Print the custom message passed to the decorator
            fun(*args, **kwargs)  # Call the original function with any arguments it may need
            print("After function")

        return wrapper

    return decorator


# @decorator_func("Hello there")
def simple(*name, **kwargs):
    print(f"Hello, {name}!")
    print(f"Kwargs, {kwargs}!")


decorator = decorator_func("Hello there")
simple = decorator(simple)

simple("Alice", "ferhat", value="data", last="ferhat")
