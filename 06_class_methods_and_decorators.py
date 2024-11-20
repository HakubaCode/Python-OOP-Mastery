# Understanding Class Methods, Static Methods, and Property Decorators
# =================================================================

class Temperature:
    """
    A class demonstrating different types of methods and property decorators
    """
    
    def __init__(self, celsius):
        self._celsius = celsius  # Protected attribute
    
    @property
    def celsius(self):
        """Property decorator - allows getting value like an attribute"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter - allows setting value with validation"""
        if value < -273.15:  # Absolute zero
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Calculated property"""
        return (self._celsius * 9/5) + 32
    
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Class method - alternative constructor"""
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)
    
    @staticmethod
    def is_valid_temperature(celsius):
        """Static method - utility function"""
        return celsius >= -273.15

# Using the class
temp = Temperature(25)  # Regular constructor
print(temp.celsius)     # Using property getter
temp.celsius = 30       # Using property setter
print(temp.fahrenheit)  # Using calculated property

# Using class method as alternative constructor
temp_f = Temperature.from_fahrenheit(98.6)
print(temp_f.celsius)

# Using static method
print(Temperature.is_valid_temperature(-300))  # False
print(Temperature.is_valid_temperature(20))    # True
