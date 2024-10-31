#!/usr/bin/python3
""" LIFOCache Class Implementation
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache using LIFO eviction policy"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = next(reversed(self.cache_data))
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key"""
        return self.cache_data.get(key)
