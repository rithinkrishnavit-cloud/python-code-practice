class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # public
        self.__balance = balance  # private (hidden)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):  # getter
        return self.__balance


acc = BankAccount("Alice", 1000)

acc.deposit(500)  # Deposited ₹500
acc.withdraw(300)  # Withdrew ₹300
print(acc.get_balance())  # 1200

# Direct access blocked
# print(acc.__balance)    AttributeError

# acc.__balance = 999999  creates a new variable, doesn't change real balance
