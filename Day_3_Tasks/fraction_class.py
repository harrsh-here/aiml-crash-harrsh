# Description: Models fractional arithmetic using magic dunder overrides, complete with structural reductions.

import math
from functools import total_ordering

@total_ordering
class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other: 'Fraction') -> 'Fraction':
        num = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other: 'Fraction') -> bool:
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)

if __name__ == "__main__":
    # @functools.total_ordering automates missing inequality dunder evaluations (__le__, __gt__, __ge__).
    # By manually supplying __eq__ and __lt__, total_ordering infers the remaining comparison conditions.

    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)
    f3 = Fraction(3, 4)

    print(f1 == f2)
    print(f1 < f3)
    print(f1 + f3)
    print(f3 > f2)