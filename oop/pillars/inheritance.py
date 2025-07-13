"""
Object-Oriented Programming Principle #2: Inheritance

Inheritance allows a class (child/subclass) to acquire behavior and data from another class (parent/superclass).

This promotes code reuse and creates "is-a" relationships — but must be used thoughtfully.
"""

# ✅ Good Example: Reusing behavior via inheritance
class Animal:
    """
    Base class with shared behavior for all animals.
    """
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} makes a sound."


class Dog(Animal):
    """
    Dog inherits from Animal and overrides speak().
    """
    def speak(self) -> str:
        return f"{self.name} barks."


class Cat(Animal):
    """
    Cat also inherits and customizes behavior.
    """
    def speak(self) -> str:
        return f"{self.name} meows."


# ❌ Anti-Example: Inheritance abuse — wrong relationship
class Engine:
    def start(self):
        return "Engine starting..."

class Car(Engine):  # ❌ Car is not an Engine
    def drive(self):
        return "Car is driving"

# This is a has-a relationship, not is-a.
# Car should contain an Engine, not inherit from it.


# ✅ Usage Example
if __name__ == "__main__":
    dog = Dog("Rex")
    cat = Cat("Whiskers")

    print(dog.speak())  # Rex barks.
    print(cat.speak())  # Whiskers meows.

    # Bad inheritance misuse
    car = Car()
    print(car.start())  # Works, but design is misleading
