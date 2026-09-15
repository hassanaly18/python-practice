class InfiniteCounter:
    def __init__(self, start=0):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current += 1
        return value  # never raises StopIteration — goes forever

counter = InfiniteCounter(1)
for num in counter:
    if num > 5:
        break
    print(num)
# 1 2 3 4 5