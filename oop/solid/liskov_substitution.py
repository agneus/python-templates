"""
Liskov Substitution Principle (LSP)

Subtypes must be usable in place of their base types without unexpected behavior.

This principle protects assumptions made by the client code.
"""

# ❌ Anti-Example: Violates LSP — subclass breaks expected behavior
class Bird:
    """
    Base class that assumes all birds can fly.
    """
    def fly(self):
        return "Flying high!"


class Sparrow(Bird):
    pass


class Penguin(Bird):
    """
    Penguins can't fly — this violates LSP if used where a Bird is expected.
    """
    def fly(self):
        raise NotImplementedError("Penguins can't fly!")


# ✅ LSP-Compliant Version: Separate flying behavior from bird identity
from abc import ABC, abstractmethod

class Bird:
    """
    General bird class with no assumptions about abilities.
    """
    pass


class Flyable(ABC):
    """
    Interface for things that can fly.
    """
    @abstractmethod
    def fly(self) -> str:
        pass


class Sparrow(Bird, Flyable):
    def fly(self) -> str:
        return "Sparrow soars!"


class Penguin(Bird):
    """
    Penguin is still a bird, but doesn't pretend to be flyable.
    """
    def swim(self) -> str:
        return "Penguin swims!"


# ✅ Usage Example
def lift_off(bird: Flyable):
    print(bird.fly())


if __name__ == "__main__":
    sparrow = Sparrow()
    lift_off(sparrow)  # ✅ Works

    penguin = Penguin()
    # lift_off(penguin)  # ❌ Static type checker would flag this (correctly)
