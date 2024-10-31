#!/usr/bin/python3
""" LRUCache Class Implementation """
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRU caching system that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache using LRU eviction policy"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Retrieve an item by key and mark it as recently used"""
        if key is None or key not in self.cache_data:
            return None
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
