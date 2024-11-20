# Understanding Inheritance in Python
# =================================

class Animal:
    """Base class (parent class)"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"

class Cat(Animal):
    """Derived class (child class) inheriting from Animal"""
    
    def __init__(self, name, breed):
        # Call parent class's __init__
        super().__init__(name, species="Cat")
        self.breed = breed
    
    def make_sound(self):
        # Override parent's method
        return "Meow!"
    
    def purr(self):
        # New method specific to Cat
        return f"{self.name} is purring..."

# Creating instances
generic_animal = Animal("Generic", "Unknown")
whiskers = Cat("Whiskers", "Siamese")

# Demonstrating inheritance
print(whiskers.name)        # Inherited attribute
print(whiskers.make_sound())  # Overridden method
print(whiskers.purr())        # Cat-specific method
