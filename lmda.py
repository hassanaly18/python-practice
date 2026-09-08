square = lambda x: x ** 2
print(square(5))  # 25

people = [{"name": "Bob", "age": 30}, {"name": "Amy", "age": 25}]
# More typical usage: inline, not assigned to a name
print(sorted(people, key=lambda p: p["age"]))
print(list(filter(lambda x: x % 2 == 0, range(10))))