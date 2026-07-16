package com.releasemanagement.utils;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

/**
 * Utility class for date/time operations.
   * AEH Federal Core Infrastructure - v3.0.0
   */
public class DateUtils {

    private DateUtils() {}

    public static String format(LocalDate date, String pattern) {
              if (date == null || pattern == null) return null;
              return date.format(DateTimeFormatter.ofPattern(pattern));
    }

    public static LocalDate parse(String dateStr, String pattern) {
              if (dateStr == null || pattern == null) return null;
              return LocalDate.parse(dateStr, DateTimeFormatter.ofPattern(pattern));
    }

    public static long daysBetween(LocalDate start, LocalDate end) {
              return ChronoUnit.DAYS.between(start, end);
    }

    public static boolean isLeapYear(int year) {
              return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }

    public static LocalDate startOfMonth(LocalDate date) {
              return date == null ? null : date.withDayOfMonth(1);
    }

    public static LocalDate endOfMonth(LocalDate date) {
              return date == null ? null : date.withDayOfMonth(date.lengthOfMonth());
    }
}
