from abc import ABC, abstractmethod

# Encapsulation
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance        # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account("Amit", 1000)
acc.deposit(500)
print("Balance:", acc.get_balance())

try:
    print(acc.__balance)
except AttributeError as e:
    print("Error:", e)

# Abstraction
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

r = Rectangle(10, 5)
print("Area of rectangle:", r.area())

try:
    s = Shape()
except TypeError as e:
    print("Error:", e)