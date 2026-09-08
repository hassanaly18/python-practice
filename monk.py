class MathOps:
    def square(self, x):
        return x * x

# Create two instances
m1 = MathOps()
m2 = MathOps()

# Define a new method
def cube(self, x):
    return x * x * x

# Patch only m1
m1.square = cube.__get__(m1)  # Replace square with cube for m1
print(m1.square(3))  # Patched version → cube
print(m2.square(3))  # Original version → square





# class B:
#     def greet(self):
#         print("Hello from B!")

# # Create instances
# b1 = B()
# b2 = B()

# # Define new method
# def new_greet(self):
#     print("Hello from monkey patch!")

# # Patch only b1
# b1.greet = new_greet.__get__(b1)  # Bind method to instance
# b1.greet() 
# b2.greet()