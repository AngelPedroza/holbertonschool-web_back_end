#!/usr/bin/python3
""" BasicCaching module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache"""""
    def __init__(self):
        """Init function"""
        super().__init__()

    def put(self, key, item):
        """Must assign value for the key."""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key is None:
            return None
        return self.cache_data.get(key, None)
