#!/usr/bin/env python3
"""Defines LRUCache class"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implement LRUCache class"""

    def __init__(self):
        super().__init__()
        self.lru_list = []

    def put(self, key, item):
        """Add an item to the cache with LRU eviction policy"""
        if key is None or item is None:
            return

        if key in self.lru_list:
            self.cache_data[key] = item

            self.lru_list.remove(key)
            self.lru_list.append(key)

            return

        if len(self.lru_list) >= self.MAX_ITEMS:
            least_key = self.lru_list.pop(0)
            del self.cache_data[least_key]

            print(f"DISCARD: {least_key}")

        self.cache_data[key] = item
        self.lru_list.append(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        value = self.cache_data.get(key)

        if value:
            self.lru_list.remove(key)
            self.lru_list.append(key)

        return value
