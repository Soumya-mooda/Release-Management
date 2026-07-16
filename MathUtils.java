package com.releasemanagement.utils;

/**
 * Utility class for common mathematical operations.
   * AEH Federal Core Infrastructure - v3.0.0
   */
public class MathUtils {

    private MathUtils() {}

    public static long factorial(int n) {
              if (n < 0) throw new IllegalArgumentException("n must be non-negative");
              long result = 1;
              for (int i = 2; i <= n; i++) result *= i;
              return result;
    }

    public static int gcd(int a, int b) {
              a = Math.abs(a);
              b = Math.abs(b);
              while (b != 0) {
                            int t = b;
                            b = a % b;
                            a = t;
              }
              return a;
    }

    public static int lcm(int a, int b) {
              if (a == 0 || b == 0) return 0;
              return Math.abs(a / gcd(a, b) * b);
    }

    public static boolean isPrime(int n) {
              if (n < 2) return false;
              if (n == 2) return true;
              if (n % 2 == 0) return false;
              for (int i = 3; (long) i * i <= n; i += 2) {
                            if (n % i == 0) return false;
              }
              return true;
    }

    public static double power(double base, int exp) {
              if (exp == 0) return 1;
              if (exp < 0) return 1.0 / power(base, -exp);
              double result = 1;
              while (exp > 0) {
                            if ((exp & 1) == 1) result *= base;
                            base *= base;
                            exp >>= 1;
              }
              return result;
    }
}
