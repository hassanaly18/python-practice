nums = [10, 20, 30]        # this is an iterable
it = iter(nums)             # this creates an iterator from it

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
print(next(it))  # raises StopIteration — nothing left