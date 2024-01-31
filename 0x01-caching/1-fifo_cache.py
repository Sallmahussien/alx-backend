#!/usr/bin/env python3
"""Defines FIFOCache class"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Implement FIFOCache class"""

    def __init__(self):
        """Initialize a new object from FIFOCache"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache with FIFO eviction policy"""
        if key is None or item is None:
            return

        if key in self.queue:
            self.cache_data[key] = item

            self.queue.remove(key)
            self.queue.append(key)
            return

        if len(self.queue) >= self.MAX_ITEMS:
            oldest_key = self.queue.pop(0)
            del self.cache_data[oldest_key]

            print(f"DISCARD: {oldest_key}")

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache"""
        return self.cache_data.get(key)
