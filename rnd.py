from random import seed, random, randint, gauss, choice, shuffle, sample

seed(1)
print(random(), random(), random())

seed(1)  # reseed with the same value
print(random(), random(), random())

seed(1)
for _ in range(5):
    print(random())

seed(1)
for _ in range(5):
    print(randint(0, 10))

seed(1)
for _ in range(5):
    print(gauss(0, 1))

seed(1)
sequence = list(range(20))
print(choice(sequence))   # picks ONE item, uniformly at random

print()
seed(1)
sequence = list(range(20))
shuffle(sequence)   # mutates the list directly — no return value
print(sequence)


print()
nums = [10, 20, 30, 40, 50]
result = sample(nums, 3)
print(result)    # e.g. [30, 20, 10] — order is random too
print(nums)      # unchanged: [10, 20, 30, 40, 50]

s = "Tutorialspoint"
print(sample(s, 3))   # e.g. ['i', 'n', 't']

t = ("Tutorialspoint", "Ankit", "Tutorix", "courses", "online")
print(sample(t, 3))


my_list = [1, 2, 3, 1, 3, 2]
try:
    sampled = random.sample(my_list, 10)
except ValueError as e:
    print("Error:", e)