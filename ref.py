import sys
import gc

a = []
print(sys.getrefcount(a))  # 2 (one from 'a', one from getrefcount's argument)

b = a
print(sys.getrefcount(a))  # 3

del b
print(sys.getrefcount(a))  # 2

gc.collect()          # force a full collection
print(gc.get_threshold())  # (700, 10, 10) by default
print(gc.get_count())  

gc.collect()          # force a full collection
print(gc.get_threshold())  # (700, 10, 10) by default
print(gc.get_count())  

gc.collect()          # force a full collection
print(gc.get_threshold())  # (700, 10, 10) by default
print(gc.get_count())  