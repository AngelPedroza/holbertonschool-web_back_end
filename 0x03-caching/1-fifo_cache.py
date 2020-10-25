#!/usr/bin/python3
""" BasicCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache"""

    def __init__(self):
        """Init the instance"""
        super().__init__()

    def put(self, key, item):
        """Assing a key to a value"""
        if key is not None or item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_discard = list(self.cache_data.keys())[0]
                del self.cache_data[to_discard]
                print("DISCARD: {}".format(to_discard))

    def get(self, key):
        """ return the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data.get(key)
