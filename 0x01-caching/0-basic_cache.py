#!/usr/bin/env python3
"""Defines BasicCache class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implement BasicCashe class"""

    def __init__(self):
        """Initialize a new object from BasicCache"""
        super().__init__()

    def put(self, key, item):
        """Assign a new key/value to the dict"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves value of a specific key from the dict"""
        if key is None or not self.cache_data.get(key):
            return None

        return self.cache_data.get(key)
