"""
Open/Closed Principle (OCP)

Classes should be open for extension, but closed for modification.

This allows you to add new behavior without changing existing, working code.
"""

# ❌ Anti-Example: Breaks OCP — requires modifying class to add new behavior
class DiscountCalculator:
    """
    Calculates discounts based on customer type.
    Each new type forces us to edit this class.
    """
    def calculate(self, customer_type, amount):
        if customer_type == "regular":
            return amount * 0.9
        elif customer_type == "vip":
            return amount * 0.8
        elif customer_type == "employee":
            return amount * 0.5
        else:
            return amount


# ✅ OCP-Compliant Version using polymorphism
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    """
    Abstract base for discount strategies.
    New strategies can be added without touching existing code.
    """
    @abstractmethod
    def apply(self, amount: float) -> float:
        pass


class RegularDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float:
        return amount * 0.9


class VIPDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float:
        return amount * 0.8


class EmployeeDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float:
        return amount * 0.5


class NoDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float:
        return amount


class DiscountCalculator:
    """
    Delegates discount logic to injected strategy.
    This class never changes when new discounts are added.
    """
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate(self, amount: float) -> float:
        return self.strategy.apply(amount)


# ✅ Usage Example
if __name__ == "__main__":
    amount = 100

    regular = DiscountCalculator(RegularDiscount())
    print("Regular:", regular.calculate(amount))

    vip = DiscountCalculator(VIPDiscount())
    print("VIP:", vip.calculate(amount))

    employee = DiscountCalculator(EmployeeDiscount())
    print("Employee:", employee.calculate(amount))
