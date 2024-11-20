# Understanding Abstract Classes in Python
# =====================================
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Abstract base class that defines a template for vehicles
    ABC ensures this class cannot be instantiated directly
    """
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def start_engine(self):
        """Must be implemented by all child classes"""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """Must be implemented by all child classes"""
        pass
    
    def horn(self):
        """Non-abstract method, provides default implementation"""
        return "Beep beep!"

class Car(Vehicle):
    def start_engine(self):
        return f"{self.brand} {self.model} engine is starting with a vroom!"
    
    def stop_engine(self):
        return f"{self.brand} {self.model} engine is stopping..."

class ElectricCar(Vehicle):
    def start_engine(self):
        return f"{self.brand} {self.model} motor is starting silently..."
    
    def stop_engine(self):
        return f"{self.brand} {self.model} motor is stopping..."

# Cannot create abstract class instance
# vehicle = Vehicle("Generic", "Brand")  # This would raise an error

# Creating concrete class instances
car = Car("Toyota", "Camry")
tesla = ElectricCar("Tesla", "Model 3")

print(car.start_engine())
print(tesla.start_engine())
print(car.horn())  # Using non-abstract method
