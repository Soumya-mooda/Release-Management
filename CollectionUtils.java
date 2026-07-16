package com.releasemanagement.utils;

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

/**
 * Utility class for common Collection operations.
   * AEH Federal Core Infrastructure - v3.0.0
   */
public class CollectionUtils {

    private CollectionUtils() {}

    public static boolean isEmpty(Collection<?> collection) {
              return collection == null || collection.isEmpty();
    }

    public static <T> List<T> filterNull(List<T> list) {
              if (list == null) return Collections.emptyList();
              return list.stream().filter(Objects::nonNull).collect(Collectors.toList());
    }

    public static <T> List<List<T>> partition(List<T> list, int size) {
              if (list == null || size <= 0) return Collections.emptyList();
              List<List<T>> partitions = new ArrayList<>();
              for (int i = 0; i < list.size(); i += size) {
                            partitions.add(list.subList(i, Math.min(i + size, list.size())));
              }
              return partitions;
    }

    public static <T, K> Map<K, List<T>> groupBy(List<T> list, Function<T, K> keyExtractor) {
              if (list == null || keyExtractor == null) return Collections.emptyMap();
              return list.stream().collect(Collectors.groupingBy(keyExtractor));
    }

    public static <T> List<T> distinct(List<T> list) {
              if (list == null) return Collections.emptyList();
              return list.stream().distinct().collect(Collectors.toList());
    }

    public static <T> Optional<T> findFirst(List<T> list, java.util.function.Predicate<T> predicate) {
              if (list == null || predicate == null) return Optional.empty();
              return list.stream().filter(predicate).findFirst();
    }
}
