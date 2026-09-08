class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius can't be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)  # alternate constructor

    @staticmethod
    def is_valid_radius(value):
        return value >= 0  # doesn't need self or cls at all

c = Circle(10)
print(c.radius)

c.radius = 20
print(c.radius)

print(c.area)

c = Circle.from_diameter(20)
print(Circle.is_valid_radius(10))


# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  # calls Animal.__init__
#         self.breed = breed



# class A:
#     def greet(self):
#         return "A"

# class B(A):
#     def greet(self):
#         return "B"

# class C(A):
#     def greet(self):
#         return "C"

# class D(B, C):
#     pass

# print(D().greet())        # "B"
# print(D.__mro__)          # (D, B, C, A, object)