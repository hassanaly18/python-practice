class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self  # the object is its own iterator

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

c = Counter(5)
# for num in c:
#     print(num)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
