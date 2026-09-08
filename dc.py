from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1)          # Point(x=1, y=2) — auto __repr__
print(p1 == p2)     # True — auto __eq__