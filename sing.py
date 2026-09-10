# Parent class 
class Animal: 
    def __init__(self, name): 
        self.name = name 
        print(f"Animal '{self.name}' created.") 
 
    def speak(self): 
        print("Animal makes a sound.") 
 
# Child class 
class Dog(Animal): 
    # We can override the parent's method 
    def speak(self): 
        print(f"{self.name} says Woof!") 
 
# Create an object of the Child class 
my_dog = Dog("Buddy") 
 
# The child object calls its own overridden method 
my_dog.speak() 

