package com.releasemanagement.utils;

import java.util.regex.Pattern;

/**
 * Utility class for common validation operations.
   * AEH Federal Core Infrastructure - v2.0.0
   */
public class ValidatorUtils {

    private ValidatorUtils() {}

    private static final Pattern EMAIL_PATTERN =
          Pattern.compile("^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$");

    private static final Pattern PHONE_PATTERN =
          Pattern.compile("^\+?[0-9]{7,15}$");

    private static final Pattern ALPHANUMERIC =
          Pattern.compile("^[a-zA-Z0-9]+$");

    public static boolean isValidEmail(String email) {
              return email != null && EMAIL_PATTERN.matcher(email.trim()).matches();
    }

    public static boolean isValidPhone(String phone) {
              return phone != null && PHONE_PATTERN.matcher(phone.trim()).matches();
    }

    public static boolean isNullOrBlank(String value) {
              return value == null || value.trim().isEmpty();
    }

    public static boolean isAlphanumeric(String value) {
              return value != null && ALPHANUMERIC.matcher(value).matches();
    }

    public static boolean isInRange(int value, int min, int max) {
              return value >= min && value <= max;
    }

    public static boolean isPositive(double value) {
              return value > 0;
    }

    public static String requireNonBlank(String value, String fieldName) {
              if (isNullOrBlank(value)) {
                            throw new IllegalArgumentException(fieldName + " must not be blank");
              }
              return value.trim();
    }
}
