# Understanding Encapsulation in Python
# ===================================

class BankAccount:
    """
    Demonstrates encapsulation by making certain attributes private
    and providing controlled access through methods
    """
    
    def __init__(self, owner, initial_balance):
        self.owner = owner                # Public attribute
        self._balance = initial_balance   # Protected attribute (single underscore)
        self.__pin = "1234"              # Private attribute (double underscore)
    
    def deposit(self, amount):
        """Public method to add money"""
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Invalid deposit amount"
    
    def _validate_pin(self, pin):
        """Protected method for pin validation"""
        return pin == self.__pin
    
    def withdraw(self, amount, pin):
        """Public method that uses private attribute validation"""
        if not self._validate_pin(pin):
            return "Invalid PIN!"
        
        if amount <= self._balance:
            self._balance -= amount
            return f"Withdrawn ${amount}. New balance: ${self._balance}"
        return "Insufficient funds"

# Creating an account
account = BankAccount("John Doe", 1000)

# Accessing public methods
print(account.deposit(500))       # Works fine
print(account.withdraw(200, "1234"))  # Works with correct PIN

# Trying to access private attributes (don't work directly)
# print(account.__pin)           # Will raise AttributeError
# print(account.__validate_pin)  # Will raise AttributeError
