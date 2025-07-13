"""
Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules.
Both should depend on abstractions.

This principle decouples systems by ensuring that details depend on abstractions, not the other way around.
"""

from abc import ABC, abstractmethod

# ❌ Anti-Example: High-level class directly depends on low-level implementation
class MySQLDatabase:
    def connect(self):
        return "Connected to MySQL"

class DataFetcher:
    """
    Directly tied to MySQL — can't reuse or swap out backend.
    """
    def __init__(self):
        self.db = MySQLDatabase()

    def fetch(self):
        return self.db.connect()


# ✅ DIP-Compliant: High-level depends on abstraction
class Database(ABC):
    @abstractmethod
    def connect(self) -> str:
        pass


class MySQLDatabase(Database):
    def connect(self) -> str:
        return "Connected to MySQL"


class PostgreSQLDatabase(Database):
    def connect(self) -> str:
        return "Connected to PostgreSQL"


class DataFetcher:
    """
    Depends on the Database abstraction, not implementation.
    """
    def __init__(self, db: Database):
        self.db = db

    def fetch(self):
        return self.db.connect()


# ✅ Usage Example
if __name__ == "__main__":
    mysql = MySQLDatabase()
    postgres = PostgreSQLDatabase()

    fetcher_mysql = DataFetcher(mysql)
    print(fetcher_mysql.fetch())

    fetcher_postgres = DataFetcher(postgres)
    print(fetcher_postgres.fetch())
