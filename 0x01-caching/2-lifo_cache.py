#!/usr/bin/env python3
"""Defines LIFOCache class"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implement LIFOCache class"""

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item to the cache with LIFO eviction policy"""
        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            self.cache_data[key] = item

            self.stack.remove(key)
            self.stack.append(key)
            return

        if len(self.stack) >= self.MAX_ITEMS:
            latest_key = self.stack.pop()
            del self.cache_data[latest_key]

            print(f"DISCARD: {latest_key}")

        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache"""
        return self.cache_data.get(key)
