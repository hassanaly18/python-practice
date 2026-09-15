from itertools import count, cycle, repeat

# count(): counts up forever from a start value, with a step
c = count(10, 2)
for _ in range(5):
    print(next(c))
# 10 12 14 16 18

# cycle(): repeats a sequence forever
colors = cycle(['red', 'green', 'blue'])
for _ in range(7):
    print(next(colors))
# red green blue red green blue red

# repeat(): repeats the same value forever (or a fixed number of times)
r = repeat('hi', 3)
print(list(r))
# ['hi', 'hi', 'hi']