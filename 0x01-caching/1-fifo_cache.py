#!/usr/bin/env python3
"""Task 1"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Representing Queue Caching"""
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keydiscard, _ = self.cache_data.popitem(False)
            print("DISCARD:", keydiscard)

    def get(self, key):
        """ return the value in self.cache_data linked to key."""
        return self.cache_data.get(key, None)
