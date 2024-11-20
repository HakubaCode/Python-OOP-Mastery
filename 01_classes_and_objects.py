# Understanding Classes and Objects in Python
# =========================================

class Dog:
    """
    A simple class to demonstrate the basic concepts of OOP
    
    This class shows:
    1. Class definition
    2. Constructor (__init__)
    3. Instance attributes
    4. Instance methods
    """
    
    def __init__(self, name, age):
        # Instance attributes
        self.name = name  # Each dog will have its own name
        self.age = age    # Each dog will have its own age
    
    def bark(self):
        # Instance method
        return f"{self.name} says: Woof!"
    
    def dog_info(self):
        return f"{self.name} is {self.age} years old"

# Creating objects (instances) of the Dog class
buddy = Dog("Buddy", 5)
max_dog = Dog("Max", 3)

# Using object methods
print(buddy.bark())        # Output: Buddy says: Woof!
print(max_dog.dog_info())  # Output: Max is 3 years old
