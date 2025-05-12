from random import choice
import string

class CreditCard:

    def __init__(self):
        self._number = self.generate()

    def generate(self):
        return "".join([choice(string.digits) for digit in range(14)])

    @property
    def number(self):
        formatted = ''
        grouped_by = 4
        current = 0
        for digit in self._number:
            formatted += digit
            current += 1
            if current == grouped_by:
                formatted += ' '
                current = 0
        return formatted

class VisaMixin:
    def generate(self):
        return f"42{super().generate()}"

class MasterCardMixin:
    def generate(self):
        return f"53{super().generate()}"

class ValidMixin:
    def generate(self):
        number = super().generate()
        return f"{number[:-1]}{self._checksum(number[:-1])}"

    def _process_digit(self, digit):
        digit = digit * 2
        if digit > 9:
            digit = sum([int(resulting_digit) for resulting_digit in str(digit)])
        return digit
    
    def _checksum(self, number):
        if len(number) != 15:
            raise ValueError("Number must be a 15-digit int.")
        sum = 0
        for idx, digit in enumerate(str(number)[::-1]):
            if idx % 2 != 0:
                sum += int(digit)
            else:
                sum += self._process_digit(int(digit))
        sum = sum % 10
        return 10 - sum


class Visa(VisaMixin, CreditCard):
    pass

class ValidVisa(ValidMixin, VisaMixin, CreditCard):
    pass

visa = Visa()
valid_visa = ValidVisa()
print(visa.number)
print(valid_visa.number)