# Description: Type-hinted arithmetic module that safely wraps operational methods, utilizing the Optional pattern.

from typing import Optional

def add(a: float, b: float) -> float:
    """Adds two floating point numbers and returns their sum."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first and returns the difference."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiplies two floating point numbers and returns their product."""
    return a * b

def divide(a: float, b: float) -> Optional[float]:
    """Divides a by b. Returns None if a division by zero is attempted."""
    if b == 0.0:
        return None
    return a / b

def power(base: float, exp: float) -> float:
    """Raises a base value to the exponent power and returns the result."""
    return base ** exp

def modulo(a: int, b: int) -> Optional[int]:
    """Calculates the integer remainder of a divided by b. Returns None if b is zero."""
    if b == 0:
        return None
    return a % b

if __name__ == "__main__":
    print(add(10.5, 4.5))
    print(divide(10.0, 0.0))
    print(power(2.0, 3.0))
    print(modulo(10, 3))
    print(modulo(10, 0))