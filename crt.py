class Person:
    def __new__(cls, *args, **kwargs):
        print("Step 1: __new__ — allocating memory")
        return super().__new__(cls)

    def __init__(self, name):
        print(f"Step 2: __init__ — setting up '{name}'")
        self.name = name

    def greet(self):
        print(f"Step 3: using the object — Hi, I'm {self.name}")

    def __del__(self):
        print(f"Step 4: __del__ — destroying '{self.name}'")

p = Person("Alice")
p.greet()
del p


# class Person:
#     def __new__(cls, *args, **kwargs):
#         print("1. Creating the instance (__new__)")
#         instance = super().__new__(cls)
#         return instance

#     def __init__(self, name):
#         print("2. Initializing the instance (__init__)")
#         self.name = name

# p = Person("Alice")

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def __del__(self):
#         print(f"Destroying {self.name}")

# p = Person("Alice")
# del p   # or p goes out of scope, or is reassigned