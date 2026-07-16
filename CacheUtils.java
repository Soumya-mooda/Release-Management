package com.releasemanagement.utils;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.TimeUnit;

/**
 * Simple in-memory LRU cache utility.
   * AEH Federal Core Infrastructure - v3.0.0
   */
public class CacheUtils<K, V> {

    private final int maxSize;
      private final long ttlMillis;
      private final Map<K, CacheEntry<V>> store;

    public CacheUtils(int maxSize, long ttl, TimeUnit unit) {
              this.maxSize = maxSize;
              this.ttlMillis = unit.toMillis(ttl);
              this.store = new LinkedHashMap<>(maxSize, 0.75f, true) {
                            @Override
                            protected boolean removeEldestEntry(Map.Entry<K, CacheEntry<V>> eldest) {
                                              return size() > maxSize;
                            }
              };
    }

    public synchronized void put(K key, V value) {
              store.put(key, new CacheEntry<>(value, System.currentTimeMillis()));
    }

    public synchronized Optional<V> get(K key) {
              CacheEntry<V> entry = store.get(key);
              if (entry == null) return Optional.empty();
              if (isExpired(entry)) {
                            store.remove(key);
                            return Optional.empty();
              }
              return Optional.of(entry.value);
    }

    public synchronized boolean containsKey(K key) {
              return get(key).isPresent();
    }

    public synchronized void invalidate(K key) {
              store.remove(key);
    }

    public synchronized void clear() {
              store.clear();
    }

    public synchronized int size() {
              return store.size();
    }

    private boolean isExpired(CacheEntry<V> entry) {
              return ttlMillis > 0 && (System.currentTimeMillis() - entry.createdAt) > ttlMillis;
    }

    private static class CacheEntry<V> {
              final V value;
              final long createdAt;
              CacheEntry(V value, long createdAt) {
                            this.value = value;
                            this.createdAt = createdAt;
              }
    }
}
