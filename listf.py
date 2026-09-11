# 1. append(obj) - Appends object at the end of the list
fruits = ['apple', 'banana']
fruits.append('cherry')
print("1. append():", fruits)

# 2. copy() - Returns a shallow copy of the list
fruits_copy = fruits.copy()
print("2. copy():", fruits_copy, "(This is a copy of the fruits list)")

# 3. clear() - Clears all contents from the list
fruits_copy.clear()
print("3. clear():", fruits_copy, "(The copied list is now empty)")

# 4. count(obj) - Returns the number of times an object appears in the list
numbers = [1, 2, 2, 3, 2, 4]
twos_count = numbers.count(2)
print(f"4. count(): The number 2 appears {twos_count} times in {numbers}")

# 5. extend(seq) - Appends the contents of a sequence to the list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print("5. extend(): list1 after extending with list2 ->", list1)

# 6. index(obj) - Returns the lowest index where the object appears
colors = ['red', 'green', 'blue', 'green']
green_index = colors.index('green')
print(f"6. index(): The first 'green' is at index {green_index} in {colors}")

# 7. insert(index, obj) - Inserts object into the list at the specified index
colors.insert(1, 'yellow')
print("7. insert(): After inserting 'yellow' at index 1 ->", colors)

# 8. pop([index]) - Removes and returns the last object (or object at given index)
popped_item = colors.pop() # Removes the last item ('green')
print(f"8. pop(): Popped item -> '{popped_item}' | Remaining list -> {colors}")

# 9. remove(obj) - Removes the first occurrence of the object from the list
colors.remove('red')
print("9. remove(): After removing 'red' ->", colors)

# 10. reverse() - Reverses the objects of the list in place
letters = ['a', 'b', 'c', 'd']
letters.reverse()
print("10. reverse():", letters)

# 11. sort() - Sorts objects of the list in place
random_numbers = [5, 2, 9, 1, 5, 6]
random_numbers.sort()
print("11. sort():", random_numbers)


print("\n========== Built-in Functions with Lists ==========\n")

sample_list = [10, 20, 30, 40, 50]
print(f"Working with sample_list: {sample_list}\n")

# 12. len(list) - Gives the total length of the list
print("12. len(): The length of the list is", len(sample_list))

# 13. max(list) - Returns the item from the list with the maximum value
print("13. max(): The maximum value is", max(sample_list))

# 14. min(list) - Returns the item from the list with the minimum value
print("14. min(): The minimum value is", min(sample_list))

# 15. list(seq) - Converts a sequence (like a tuple or string) into a list
sample_tuple = ('x', 'y', 'z')
converted_list = list(sample_tuple)
print(f"15. list(): Converted tuple {sample_tuple} into a list ->", converted_list)

# 16. cmp(list1, list2) 
# Note: The cmp() function was mentioned in your text, but it was removed in Python 3. 
# To compare lists in modern Python, you just use the standard comparison operators (==, <, >).
list_a = [1, 2, 3]
list_b = [1, 2, 3]
print("\n16. list comparison (replaces cmp()): Does list_a == list_b?", list_a == list_b)