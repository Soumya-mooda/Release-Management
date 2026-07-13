def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def calculator():
    """Simple command-line calculator."""
    print("=== Dummy Calculator ===")
    print("Operations: +  -  *  /")

    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ").strip()
    b = float(input("Enter second number: "))

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if op not in operations:
        print(f"Unknown operator '{op}'.")
        return

    result = operations[op](a, b)
    print(f"Result: {a} {op} {b} = {result}")


if __name__ == "__main__":
    calculator()
