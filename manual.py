import tracemalloc

tracemalloc.start()

x = [1, 2, 3]
y = x        # y points to the same list object, not a copy
y.append(4)
print(x)     # [1, 2, 3, 4]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")

for stat in top_stats[:5]:
    print(stat)