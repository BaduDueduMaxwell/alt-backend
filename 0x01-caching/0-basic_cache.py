#!/usr/bin/python3
""" BaseCache Class Implementation
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching"""

    def put(self, key, item):
        """Assign dictionary to cache_data"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key"""
        return self.cache_data.get(key)
