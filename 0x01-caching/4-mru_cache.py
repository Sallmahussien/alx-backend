#!/usr/bin/env python3
"""Defines MRUCache class"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Implement MRUCache class"""

    def __init__(self):
        super().__init__()
        self.mru = None

    def put(self, key, item):
        """Add an item to the cache with MRU eviction policy"""
        if key is None or item is None:
            return None

        if (len(self.cache_data.keys()) >= self.MAX_ITEMS and
                key not in self.cache_data.keys()):
            del self.cache_data[self.mru]
            print(f"DISCARD: {self.mru}")

        self.cache_data[key] = item
        self.mru = key

    def get(self, key):
        """Retrieve an item from the cache"""
        value = self.cache_data.get(key)

        if value:
            self.mru = key

        return value
