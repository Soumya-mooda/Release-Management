def add_three_numbers(a, b, c):
    """Return the sum of three numbers.

    Args:
        a: First number.
        b: Second number.
        c: Third number.

    Returns:
        The sum of a, b, and c.
    """
    return a + b + c


if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    result = add_three_numbers(num1, num2, num3)
    print(f"Sum of {num1}, {num2}, and {num3} = {result}")
