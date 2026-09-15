class EvenNumbers:
    def __init__(self, max_val):
        self.max_val = max_val
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max_val:
            raise StopIteration
        result = self.n
        self.n += 2
        return result

for even in EvenNumbers(10):
    print(even)
# 0 2 4 6 8 10