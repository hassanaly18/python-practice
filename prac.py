# cache = {}

# def get_user_tags(user_id):
#     try:
#         return cache[user_id]
#     except KeyError:
#         tags = fetch_tags_from_db(user_id)
#         cache[user_id] = tags
#         return tags

# get_user_tags(23)


# from functools import partial

# def power(base, exponent):
#     return base ** exponent

# square = partial(power, exponent=2)
# cube = partial(power, exponent=3)

# print(square(5))
# print(cube(5))


# from itertools import groupby
# data = [1, 1, 2, 2, 2, 3, 1, 1]
# result = [(value, sum(1 for _ in group))
#           for value, group in groupby(data)]
# print(result)


# from contextlib import contextmanager

# @contextmanager
# def suppress_and_log():
#     try:
#         yield
#     except Exception as e:
#         print("Error occured:", e)

# with suppress_and_log():
#     print("Hello")
#     print(10 / 0)
#     print("This won't run")



# squares = (n**2 for n in range(1, 1_000_001) if n % 2 == 0)
# print(squares)
# print(*squares)


# words = ["apple", "fig", "banana", "kiwi", "pear"]

# result = {word: len(word) for word in words if len(word) > 3}
# print(result)



# def append_to(item, lst=[]):
#     lst.append(item)
#     return lst

# print(append_to(1))  # [1]
# print(append_to(2))  # [1, 2]  <- surprise! same list reused


# from itertools import chain, groupby
# from functools import reduce, partial, lru_cache

# # chain: flatten multiple iterables into one
# print("Flattening iterables:", list(chain([1, 2], [3, 4])))  # [1, 2, 3, 4]

# # groupby: group consecutive items (data must be sorted for meaningful groups)
# data = [("a", 1), ("a", 2), ("b", 3)]
# for key, group in groupby(data, key=lambda x: x[0]):
#     print(key, list(group))

# # reduce: fold a sequence into a single value
# print("reduced value", reduce(lambda acc, x: acc + x, [1, 2, 3, 4]))  # 10

# # partial: pre-fill some arguments of a function
# add = lambda x, y: x + y
# add_five = partial(add, 5)
# print("Partial:", add_five(10))  # 15

# # lru_cache: memoize a function automatically
# @lru_cache(maxsize=None)
# def fib(n):
#     return n if n < 2 else fib(n-1) + fib(n-2)
    
# print("Fibonacci:", fib(8))

# squares = [x**2 for x in range(10)]
# print(squares)

# square_map = {x: x**2 for x in range(10)}
# print(square_map)

# unique_lengths = {len(word) for word in ["hi", "bye", "ok"]} #set
# print(unique_lengths)

# squares_gen = (x**2 for x in range(10))
# print(*squares_gen)

# from contextlib import contextmanager

# @contextmanager
# def timer():
#     import time
#     start = time.time()
#     yield
#     print(f"Took {time.time() - start}s")

# with timer():
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello")