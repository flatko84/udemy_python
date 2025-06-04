import unittest


class BankAccount:
    def __init__(self, initial_balance: float=0) -> None:
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        """Deposit money to the account.
        
        Arguments:
        amount - the amount to deposit
        """
        if type(amount) not in [int, float]:
            raise ValueError("The amount must be a number.")
        if amount > 0:
            self.balance += amount
        print(f"Deposited ${amount}.")

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account.
        
        Arguments:
        amount - the amount to withdraw
        """
        if type(amount) not in [int, float]:
            raise ValueError("The amount must be a number.")
        if amount > 0:
            self.balance -= amount
        print(f"Withdrawn ${amount}.")

    def __repr__(self) -> str:
        return f"A {"".join([cl.__name__ for cl in type(self).__mro__][:-1])} with ${self.balance} in it"


class Savings(BankAccount):
    INTEREST_RATE = 0.0035

    def pay_interest(self) -> None:
        """Pay interest to the bank."""
        self.deposit(self.INTEREST_RATE * self.balance)

class HighInterest(Savings):
    INTEREST_RATE = 0.007

    def __init__(self, initial_balance: float=0, withdrawal_fee: float=5) -> None:
        super().__init__(initial_balance)
        self.withdrawal_fee = withdrawal_fee

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account, withdrawal fee applies."""
        super().withdraw(amount)
        self.balance -= self.withdrawal_fee

class LockedIn(HighInterest):
    INTEREST_RATE = 0.009

    def withdraw(self, amount: float) -> None:
        """No withdrawal allowed for locked in accounts."""
        raise NotImplementedError("Cannot withdraw on demand.")
    
class BankAccountTest(unittest.TestCase):
    def test_bank_account(self):

        b = BankAccount(100)
        print(b)
        b.deposit(2)
        b.withdraw(70)
        assert(b.balance == 32)
        s = Savings(140)
        s.pay_interest()
        assert(s.balance == 140.49)
        hi = HighInterest(withdrawal_fee=3)
        hi.deposit(140)
        hi.pay_interest()
        print(hi)
        hi.withdraw(0.98)
        assert(hi.balance == 137)
        l = LockedIn(1000)
        l.pay_interest()
        withdraw_not_implemented = False
        try:
            l.withdraw(9)
        except NotImplementedError:
            withdraw_not_implemented = True
        assert(withdraw_not_implemented)
        assert(l.balance == 1009)


if __name__ == '__main__':
    unittest.main()