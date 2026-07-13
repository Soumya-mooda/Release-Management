import math


def is_prime(n):
      """Return True if n is a prime number, False otherwise.

          Args:
                  n: Integer to test.

                      Returns:
                              Boolean indicating whether n is prime.
                                  """
      if n < 2:
                return False
            if n == 2:
                      return True
                  if n % 2 == 0:
                            return False
                        for i in range(3, int(math.isqrt(n)) + 1, 2):
                                  if n % i == 0:
                                                return False
                                        return True


def primes_up_to(limit):
      """Return a list of all prime numbers up to limit (inclusive).

          Args:
                  limit: Upper bound (inclusive).

                      Returns:
                              List of prime numbers.
                                  """
    return [n for n in range(2, limit + 1) if is_prime(n)]


if __name__ == "__main__":
      num = int(input("Enter a number: "))
    if is_prime(num):
              print(f"{num} is a prime number.")
else:
        print(f"{num} is NOT a prime number.")
    limit = int(input("List all primes up to: "))
    print(f"Primes up to {limit}: {primes_up_to(limit)}")
