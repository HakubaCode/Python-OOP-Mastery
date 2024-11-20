# Understanding Polymorphism in Python
# ==================================

class Shape:
    """Base class demonstrating polymorphism"""
    def calculate_area(self):
        pass
    
    def describe(self):
        return "I am a shape"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def describe(self):
        return f"I am a rectangle with width {self.width} and height {self.height}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius ** 2
    
    def describe(self):
        return f"I am a circle with radius {self.radius}"

# Function demonstrating polymorphism
def print_shape_info(shape):
    """
    This function works with any shape object
    demonstrating polymorphic behavior
    """
    print(shape.describe())
    print(f"Area: {shape.calculate_area()}")

# Creating different shapes
rectangle = Rectangle(5, 3)
circle = Circle(4)

# Same function works with different shapes
print_shape_info(rectangle)
print_shape_info(circle)
