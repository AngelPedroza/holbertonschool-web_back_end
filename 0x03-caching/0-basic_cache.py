#!/usr/bin/python3
""" BasicCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache"""""

    def put(self, key, item):
        """Must assign value for the key."""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data.get(key)