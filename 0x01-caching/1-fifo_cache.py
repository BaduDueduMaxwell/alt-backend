#!/usr/bin/python3
""" FIFOCache Class Implementation
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def put(self, key, item):
        """Assign dictionary to cache_data"""
        if key is not None or item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = next(iter(self.cache_data))
                del self.cache_data[oldest_key]
                print(f"DISCARD {oldest_key}")

            self.cache_data[key] = item
        
    def get(self, key):
        """Retrieve an item by key"""
        return self.cache_data.get(key)