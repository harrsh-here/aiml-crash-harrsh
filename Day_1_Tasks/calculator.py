# Program to build a simple calculator using multiple functions.

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    return "Error: Division by zero" if b == 0 else a / b

ops = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}

try:
    n1, n2 = float(input("First: ")), float(input("Second: "))
    op = input("Operation (add, subtract, multiply, divide): ").strip().lower()
    print(f"Result: {ops[op](n1, n2)}" if op in ops else "Invalid operation.")

except Exception as e: 
    print(f"Error: {e}")
