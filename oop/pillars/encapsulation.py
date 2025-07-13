"""
Object-Oriented Programming Principle #1: Encapsulation

Encapsulation bundles related data and behavior together inside a class,
and restricts direct access to internal state.

This helps enforce business logic, protect invariants, and prevent misuse.
"""

# ✅ Good Example: Encapsulated BankAccount
class BankAccount:
    """
    Represents a bank account with private balance.
    Balance is accessed and modified only via public methods.
    """
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount: float):
        """
        Adds money to the account.
        Only positive amounts are accepted.
        """
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount: float):
        """
        Withdraws money if funds are sufficient.
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self) -> float:
        """
        Returns the current balance.
        """
        return self.__balance


# ❌ Anti-Example: No Encapsulation
class LooseAccount:
    """
    Balance is publicly accessible — anyone can tamper with it.
    """
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance  # exposed directly


# ✅ Usage Example
if __name__ == "__main__":
    acc = BankAccount("Alice", 1000)
    acc.deposit(200)
    acc.withdraw(100)
    print(acc.get_balance())  # ✅ 1100

    loose = LooseAccount("Bob", 1000)
    loose.balance = -9999     # ❌ Breaks business logic
    print(loose.balance)      # ❌ Garbage state
