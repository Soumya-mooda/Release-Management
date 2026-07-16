package com.releasemanagement.utils;

import java.util.HashMap;
import java.util.Map;

/**
 * Utility class for common String operations.
   * AEH Federal Core Infrastructure - v3.0.0
   */
public class StringUtils {

    private StringUtils() {
              // Utility class - prevent instantiation
    }

    /**
     * Reverses the given string.
       *
       * @param input the string to reverse
       * @return the reversed string, or null if input is null
       */
    public static String reverse(String input) {
              if (input == null) return null;
              return new StringBuilder(input).reverse().toString();
    }

    /**
     * Checks whether a string is a palindrome (case-insensitive).
       *
       * @param input the string to check
       * @return true if the string is a palindrome, false otherwise
       */
    public static boolean isPalindrome(String input) {
              if (input == null) return false;
              String cleaned = input.toLowerCase().replaceAll("[^a-z0-9]", "");
              return cleaned.equals(new StringBuilder(cleaned).reverse().toString());
    }

    /**
     * Counts the frequency of each character in the given string.
       *
       * @param input the string to analyse
       * @return a map of character to frequency count
       */
    public static Map<Character, Integer> charFrequency(String input) {
              Map<Character, Integer> freq = new HashMap<>();
              if (input == null) return freq;
              for (char c : input.toCharArray()) {
                            freq.merge(c, 1, Integer::sum);
              }
              return freq;
    }

    /**
     * Converts a camelCase string to snake_case.
       *
       * @param camel the camelCase string
       * @return the snake_case equivalent
       */
    public static String camelToSnake(String camel) {
              if (camel == null) return null;
              return camel.replaceAll("([a-z])([A-Z])", "$1_$2").toLowerCase();
    }
}
