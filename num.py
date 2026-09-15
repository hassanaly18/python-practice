import numpy as np
import time
import sys

SIZE = 1_000_000
L1, L2 = range(SIZE), range(SIZE)
A1, A2 = np.arange(SIZE), np.arange(SIZE)

start = time.time()
result = [(x, y) for x, y in zip(L1, L2)]
print((time.time() - start) * 1000)   # ~380ms

start = time.time()
result = A1 + A2
print((time.time() - start) * 1000)   # ~50ms

print()
S = range(1000)
print(sys.getsizeof(5) * len(S))   # 14000 — rough list-of-ints estimate

D = np.arange(1000)
print(D.size * D.itemsize)          # 4000 — actual packed array size


print()
a = np.array([1, 2, 3])            # 1D array — one axis, length 3
b = np.array([(1, 2, 3), (4, 5, 6)])  # 2D array — two axes: 2 rows, 3 columns
print(b)


print(np.zeros((3, 4)))              # all zeros, shape (3,4)
print(np.ones((2, 3, 4), dtype=np.int16))  # all ones, specified dtype
print(np.empty((2, 3)))               # uninitialized — contents are whatever memory happened to hold


print(np.arange(10, 30, 5))     # [10, 15, 20, 25] — like range(), but returns an array
print(np.linspace(0, 2, 9))      # 9 evenly spaced numbers from 0 to 2 — safer than arange with floats,
                           # since arange's element count with float steps can be unpredictable
                           # due to floating-point precision

print()
a = np.arange(15).reshape(3, 5)
print(a)
print(a.ndim)      # 2
print(a.shape)     # (3, 5)
print(a.size)       # 15
print(a.dtype)      # int64
print(a.itemsize)  # 8


print()
c = np.array([20, 30, 40, 50])
b = np.arange(4)

print(c - b)      # [20 29 38 47]
print(b ** 2)      # [0 1 4 9]
print(c < 35)      # [True True False False] — comparisons also elementwise

print()
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

print(A * B)     # elementwise product: [[2,0],[0,4]]
print(A @ B)     # actual matrix product: [[5,4],[3,4]]
print(A.dot(B))  # same as @

print()
C = np.arange(3)
print(np.exp(C))    # [1. 2.71828183 7.3890561]
print(np.sqrt(C))   # [0. 1. 1.41421356]


print()
d = np.arange(12).reshape(3, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(d.sum())            # 66 — sum of everything
print(d.sum(axis=0))      # [12 15 18 21] — sum DOWN each column
print(d.min(axis=1))      # [0 4 8] — min ACROSS each row

print()
a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
b = a
b is a   # True — same object, exactly like Python variable assignment in general

c = a.view()
c is a           # False — different array object
c.base is a      # True — but c's data IS a's data
c[0, 0] = 9999
print(a)         # a changed too! The data is shared.