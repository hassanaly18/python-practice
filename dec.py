from functools import wraps

def my_decorator(func):
    @wraps(func)  # preserves func.__name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper





# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

# @repeat(times=3)
# def greet(name):
#     print(f"Hello, {name}")

# greet("Sam")
# # Hello, Sam
# # Hello, Sam
# # Hello, Sam





# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} returned {result}")
#         return result
#     return wrapper

# @my_decorator
# def add(a, b):
#     return a + b

# print(add(2, 3))
# # Calling add
# # add returned