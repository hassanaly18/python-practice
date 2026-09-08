from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

s = Shape()   # TypeError: Can't instantiate abstract class
sq = Square(4)  # works fine, area() is implemented