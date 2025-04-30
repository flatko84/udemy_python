class BankAccount:
    def __init__(self, initial_balance = 0):
        self.balance = initial_balance

    def deposit(self, amount):
        if type(amount) not in [int, float]:
            raise ValueError("The amount must be a number.")
        if amount > 0:
            self.balance += amount
        print(f"Deposited ${amount}.")

    def withdraw(self, amount):
        if type(amount) not in [int, float]:
            raise ValueError("The amount must be a number.")
        if amount > 0:
            self.balance -= amount
        print(f"Withdrawn ${amount}.")

    def __repr__(self):
        return f"A {"".join([cl.__name__ for cl in type(self).__mro__][:-1])} with ${self.balance} in it"


class Savings(BankAccount):
    INTEREST_RATE = 0.0035

    def pay_interest(self):
        self.deposit(self.INTEREST_RATE * self.balance)

class HighInterest(Savings):
    INTEREST_RATE = 0.007

    def __init__(self, initial_balance=0, withdrawal_fee=5):
        super().__init__(initial_balance)
        self.withdrawal_fee = withdrawal_fee

    def withdraw(self, amount):
        super().withdraw(amount)
        self.balance -= self.withdrawal_fee

class LockedIn(HighInterest):
    INTEREST_RATE = 0.009

    def withdraw(self, amount):
        raise NotImplementedError("Cannot withdraw on demand.")
    

b = BankAccount(100)
print(b)
b.deposit(2)
b.withdraw(70)
print(b)
s = Savings(140)
print(s)
s.pay_interest()
print(s)
hi = HighInterest(withdrawal_fee=3)
hi.deposit(140)
hi.pay_interest()
print(hi)
hi.withdraw(0.98)
print(hi)
l = LockedIn(1000)
print(l)
l.pay_interest()
#l.withdraw(9)
print(l)