"""
Object-Oriented Programming Principle #3: Polymorphism

Polymorphism lets different classes implement the same interface (method name) with different behavior.

This allows code to be written in a generic way, working across different object types.
"""

from abc import ABC, abstractmethod

# ✅ Good Example: Polymorphism via shared interface
class Animal(ABC):
    """
    Abstract base class defining a shared contract: speak().
    """
    @abstractmethod
    def speak(self) -> str:
        pass


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"


class Bird(Animal):
    def speak(self) -> str:
        return "Chirp!"


def animal_speak(animal: Animal):
    """
    Works for any Animal — no need to know the concrete type.
    """
    print(animal.speak())


# ❌ Anti-Example: No polymorphism — fragile and rigid
def hardcoded_speak(animal_type: str):
    if animal_type == "dog":
        print("Woof!")
    elif animal_type == "cat":
        print("Meow!")
    elif animal_type == "bird":
        print("Chirp!")
    else:
        print("Unknown animal")


# ✅ Usage Example
if __name__ == "__main__":
    animals = [Dog(), Cat(), Bird()]
    for a in animals:
        animal_speak(a)  # Clean, extensible

    # Bad: adding a new animal requires changing function logic
    hardcoded_speak("dog")
