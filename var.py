x = [1, 2, 3]
y = x        # y points to the same list object, not a copy
y.append(4)
print(x)     # [1, 2, 3, 4]