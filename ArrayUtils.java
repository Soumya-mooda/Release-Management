package com.releasemanagement.utils;

import java.util.Arrays;

/**
 * Utility class for common array operations.
   * AEH Federal Core Infrastructure - v3.0.0
   */
public class ArrayUtils {

    private ArrayUtils() {}

    public static int[] bubbleSort(int[] arr) {
              if (arr == null) return null;
              int[] copy = Arrays.copyOf(arr, arr.length);
              for (int i = 0; i < copy.length - 1; i++) {
                            for (int j = 0; j < copy.length - i - 1; j++) {
                                              if (copy[j] > copy[j + 1]) {
                                                                    int tmp = copy[j];
                                                                    copy[j] = copy[j + 1];
                                                                    copy[j + 1] = tmp;
                                              }
                            }
              }
              return copy;
    }

    public static int binarySearch(int[] sortedArr, int target) {
              if (sortedArr == null) return -1;
              int lo = 0, hi = sortedArr.length - 1;
              while (lo <= hi) {
                            int mid = lo + (hi - lo) / 2;
                            if (sortedArr[mid] == target) return mid;
                            else if (sortedArr[mid] < target) lo = mid + 1;
                            else hi = mid - 1;
              }
              return -1;
    }

    public static int max(int[] arr) {
              if (arr == null || arr.length == 0) throw new IllegalArgumentException("Array is empty");
              int max = arr[0];
              for (int v : arr) if (v > max) max = v;
              return max;
    }

    public static int min(int[] arr) {
              if (arr == null || arr.length == 0) throw new IllegalArgumentException("Array is empty");
              int min = arr[0];
              for (int v : arr) if (v < min) min = v;
              return min;
    }

    public static double average(int[] arr) {
              if (arr == null || arr.length == 0) return 0;
              long sum = 0;
              for (int v : arr) sum += v;
              return (double) sum / arr.length;
    }

    public static int[] reverse(int[] arr) {
              if (arr == null) return null;
              int[] copy = Arrays.copyOf(arr, arr.length);
              for (int i = 0, j = copy.length - 1; i < j; i++, j--) {
                            int tmp = copy[i]; copy[i] = copy[j]; copy[j] = tmp;
              }
              return copy;
    }
}
