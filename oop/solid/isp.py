"""
Interface Segregation Principle (ISP)

Clients should not be forced to depend on interfaces they do not use.

Split large, fat interfaces into smaller, specific ones so that implementing classes only need to define what they actually support.
"""

from abc import ABC, abstractmethod

# ❌ Anti-Example: Bloated interface forces unused methods
class MultiFunctionBird(ABC):
    @abstractmethod
    def fly(self): pass

    @abstractmethod
    def swim(self): pass

    @abstractmethod
    def walk(self): pass


class Crow(MultiFunctionBird):
    def fly(self):
        return "Crow flies."

    def swim(self):
        raise NotImplementedError("Crow can't swim.")

    def walk(self):
        return "Crow walks."


# ✅ ISP-Compliant: Split interfaces into focused capabilities
class Flyable(ABC):
    @abstractmethod
    def fly(self): pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self): pass

class Walkable(ABC):
    @abstractmethod
    def walk(self): pass


class Crow(Flyable, Walkable):
    def fly(self):
        return "Crow flies."

    def walk(self):
        return "Crow walks."


class Duck(Flyable, Swimmable, Walkable):
    def fly(self):
        return "Duck flies."

    def swim(self):
        return "Duck swims."

    def walk(self):
        return "Duck waddles."


# ✅ Usage Example
def take_off(bird: Flyable):
    print(bird.fly())

def dive(bird: Swimmable):
    print(bird.swim())

def stroll(bird: Walkable):
    print(bird.walk())

if __name__ == "__main__":
    crow = Crow()
    duck = Duck()

    take_off(crow)
    stroll(crow)
    # dive(crow)  # ❌ Won't work — Crow can't swim, and shouldn't pretend

    take_off(duck)
    dive(duck)
    stroll(duck)
