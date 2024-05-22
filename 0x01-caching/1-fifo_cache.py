#!/usr/bin/python3
""" 1-fifo_cache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize the class and call the parent init method
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assign to dictionary self.cache_data the item value for the key key.

        Args:
            key: The key to be added to the cache.
            item: The item to be added to the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.order.pop(0)
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Return the value in self.cache_data linked to key.

        Args:
            key: The key to retrieve from the cache.

        Returns:
            The value associated with the key,
            or None if key is None or doesn't exist.
        """
        return self.cache_data.get(key, None)
