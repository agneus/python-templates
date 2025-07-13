"""
Object-Oriented Programming Principle #4: Abstraction

Abstraction hides complex implementation details and exposes only what’s necessary through a clean interface.

It lets you focus on *what* an object does, not *how* it does it.
"""

from abc import ABC, abstractmethod

# ✅ Good Example: Abstract class defines behavior without revealing implementation
class PaymentProcessor(ABC):
    """
    Abstract interface for any payment system.
    Clients rely on this, not the details underneath.
    """
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class StripeProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using Stripe."


class PayPalProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using PayPal."


def process_payment(processor: PaymentProcessor, amount: float):
    """
    Works with any payment processor that adheres to the PaymentProcessor interface.
    """
    print(processor.pay(amount))


# ❌ Anti-Example: No abstraction — hardcoded dependency
class Store:
    def checkout(self, amount: float):
        stripe = StripeProcessor()  # tightly coupled
        print(stripe.pay(amount))   # can't swap, test, or reuse easily


# ✅ Usage Example
if __name__ == "__main__":
    stripe = StripeProcessor()
    paypal = PayPalProcessor()

    process_payment(stripe, 100.0)
    process_payment(paypal, 50.0)

    # Anti-pattern: bad design
    store = Store()
    store.checkout(30.0)
