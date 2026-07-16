def fibonacci(n):
      """Return a list of the first n Fibonacci numbers."""
      if n <= 0:
                return []
            series = [0, 1]
    for _ in range(2, n):
              series.append(series[-1] + series[-2])
          return series[:n]


def print_fibonacci(n):
      """Print the Fibonacci series up to n terms."""
    result = fibonacci(n)
    print(f"Fibonacci series ({n} terms): {result}")


if __name__ == "__main__":
      terms = int(input("Enter the number of terms: "))
    if terms <= 0:
              print("Please enter a positive integer.")
else:
        print_fibonacci(terms)
