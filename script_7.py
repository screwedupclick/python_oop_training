# static methods

# A static method in python is a method that belongs to the class itself rather than any instance of the class

# To define a static method, we use the '@staticmethod' decorator

# static vs instane method exemple

class BankAccount:
    MIN_BALANCE = 100
    
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit", amount)
            print(f"{self.owner}'s new balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")
            
    def _is_valid_amount(self, amount):
        return amount > 0
    
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. New balance: ${self._balance}")
            
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
account = BankAccount("Alice", 500)
account.deposit(200)

account.__log_transaction("withdraw", 300)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))