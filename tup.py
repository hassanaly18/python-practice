empty_tuple = ()
print("Empty tuple:", empty_tuple)

int_tuple = (1, 2, 3)
print("Integer tuple:", int_tuple)

mixed_tuple = (1, "Hello", 3.4)
print("Mixed tuple:", mixed_tuple)

nested_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print("Nested tuple:", nested_tuple)

# Tuple packing (parentheses are optional)
packed_tuple = 3, 4.6, "dog"
print("Packed tuple:", packed_tuple)

# Tuple unpacking
a, b, c = packed_tuple
print(f"Unpacked variables: a={a}, b={b}, c={c}")

# Single element tuple (requires a trailing comma)
not_a_tuple = ("hello")
real_tuple = ("hello",)
print(f"Type of ('hello'): {type(not_a_tuple)}")
print(f"Type of ('hello',): {type(real_tuple)}")


print("\n========== 2. Accessing Elements ==========\n")

my_tuple = ('p','r','o','g','r','a','m','i','z')

print("Index 0:", my_tuple[0])
print("Index 5:", my_tuple[5])

# Negative indexing
print("Last item (-1):", my_tuple[-1])
print("Second to last (-2):", my_tuple[-2])

# Nested indexing
print("Nested index access n_tuple[1][1]:", nested_tuple[1][1])

# Slicing
print("Slice [1:4]:", my_tuple[1:4])
print("Slice [:-7]:", my_tuple[:-7])
print("Slice [7:]:", my_tuple[7:])
print("Slice [:] (copy):", my_tuple[:])


print("\n========== 3. Changing or Deleting a Tuple ==========\n")

# Tuples are immutable, so item assignment throws a TypeError
# my_tuple[1] = 'x'  # Uncommenting this raises a TypeError

mutable_in_tuple = (4, 2, 3, [6, 5])
print("Original tuple with list:", mutable_in_tuple)
# But we CAN change mutable items (like lists) inside the tuple
mutable_in_tuple[3][0] = 9
print("Tuple after changing nested list:", mutable_in_tuple)

# Concatenation and Repetition
concat_tuple = (1, 2, 3) + (4, 5, 6)
print("Concatenation (+):", concat_tuple)

repeat_tuple = ("Repeat",) * 3
print("Repetition (*):", repeat_tuple)

# Deleting (You can't delete an item, but you can delete the whole tuple)
temp_tuple = (1, 2, 3)
del temp_tuple
# print(temp_tuple) # Uncommenting this raises NameError because it's deleted


print("\n========== 4. Python Tuple Methods ==========\n")

apple_tuple = ('a','p','p','l','e',)

# count(x) - Returns number of times x appears
print("Count of 'p':", apple_tuple.count('p'))

# index(x) - Returns first index of x
print("Index of 'l':", apple_tuple.index('l'))


print("\n========== 5. Other Tuple Operations ==========\n")

# Membership testing
print("Is 'a' in tuple?", 'a' in apple_tuple)
print("Is 'b' in tuple?", 'b' in apple_tuple)
print("Is 'g' not in tuple?", 'g' not in apple_tuple)

# Iteration
print("Iterating through tuple:")
for name in ('John', 'Kate'):
    print(" - Hello", name)


print("\n========== 6. Built-in Functions with Tuple ==========\n")

num_tuple = (5, 2, 9, 1, 7)
bool_tuple = (True, True, False)

print(f"Working with num_tuple: {num_tuple}")

# all() - True if all elements are true
print("all() of bool_tuple:", all(bool_tuple))

# any() - True if any element is true
print("any() of bool_tuple:", any(bool_tuple))

# enumerate() - Returns pairs of (index, value)
print("enumerate() of num_tuple:", list(enumerate(num_tuple)))

# len() - Number of items
print("len():", len(num_tuple))

# max() - Largest item
print("max():", max(num_tuple))

# min() - Smallest item
print("min():", min(num_tuple))

# sorted() - Returns a new sorted LIST
print("sorted():", sorted(num_tuple), "(Notice this returns a list)")

# sum() - Sum of all items
print("sum():", sum(num_tuple))

# tuple() - Converts an iterable to a tuple
string_iterable = "hello"
print(f"tuple() converting string '{string_iterable}':", tuple(string_iterable))