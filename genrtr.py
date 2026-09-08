def inner_gen():
    yield 1
    yield 2

def outer_gen():
    yield "start"
    yield from inner_gen()  
    yield "end"

print(list(outer_gen()))  # ['start', 1, 2, 'end']



def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# gen = count_up_to(5)
# print(next(gen))  # 1
# print(next(gen))  # 2

# for x in count_up_to(5):
#     print(x)  # 1 2 3 4 5

def get_numbers():
    yield 1
    yield 2
    yield 3

numbers = get_numbers()
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))


def numbers():
    for i in range(1, 1_000_000_001):
        yield i

# for n in numbers():
#     print(n)