#!/usr/bin/env python3
"""Task 0"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Representing the Basic Caching system"""
    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key"""
        if key == None or item == None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data
        linked to key."""
        return self.cache_data.get(key, None)
