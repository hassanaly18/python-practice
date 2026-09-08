def shout(text):
    return text.upper()

# def whisper(text):
#     return text.lower()

# # Store functions in a list
# funcs = [shout, whisper]
# for f in funcs:
#     print(f("Hello"))  # HELLO, then hello

# # Store in a dict, use as a dispatch table
# actions = {"shout": shout, "whisper": whisper}
# print(actions["shout"]("hi"))  # HI


def apply_twice(func, value):
    return func(func(value))

print(apply_twice(shout, "hi"))  # "HI" (shout is idempotent here, but you get the idea)

people = [{"name": "Bob", "age": 30}, {"name": "Amy", "age": 25}]
sorted_people = sorted(people, key=lambda p: p["age"])
print(sorted_people)