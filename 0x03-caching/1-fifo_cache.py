#!/usr/bin/python3
""" BasicCaching module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache"""

    def __init__(self):
        """Init the instance"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Assing a key to a value"""
        if key is not None or item is not None:

            if key not in self.stack:
                self.stack.append(key)
            else:
                self.move_to_last_in(key)

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_discard = self.stack[0]
                if to_discard:
                    self.stack.remove(to_discard)
                    del self.cache_data[to_discard]
                    print("DISCARD: {}".format(to_discard))

    def get(self, key):
        """ return the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

    def move_to_last_in(self, key):
        """Move an element to the init the list"""
        if self.stack[-1] != key:
            self.stack.remove(key)
            self.stack.append(key)
