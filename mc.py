class MyMeta(type):
    def __new__(cls, name, bases, namespace):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, namespace)

class MyClass(metaclass=MyMeta):
    pass
# prints: Creating class MyClass