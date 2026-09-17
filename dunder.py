class Distance:

    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __ge__(self, other):
        total1 = self.feet * 12 + self.inches
        total2 = other.feet * 12 + other.inches

        return total1 >= total2

    def __add__(self, other):
        temp = Distance(
            self.feet + other.feet,
            self.inches + other.inches
        )

        if temp.inches >= 12:
            temp.feet += 1
            temp.inches -= 12

        return temp

d1 = Distance(2, 1)
d2 = Distance(4, 10)

print(d1 >= d2)

d3 = d1 + d2
print(d3)



# class User:

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

#     def __repr__(self):
#         return f"User(name={self.name!r})"

#     def __eq__(self, other):
#         return self.name == other.name

# user = User("Hassan")

# u1 = User("Hassan")
# u2 = User("Hassan")

# print(str(user))
# print(repr(user))
# print(u1==u2)


# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return Number(self.value + other.value)

# a = Number(10)
# b = Number(20)

# c = a + b
# print(c.value)

# print(dir(int))

# class Person:
#     def __init__(self, name):
#         self.name = name

# box = Box(10)