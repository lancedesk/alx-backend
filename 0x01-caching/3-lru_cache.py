#!/usr/bin/python3
"""
3-lru_cache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize the class and call the parent init method
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assign to dictionary self.cache_data the item value for the key key.

        Args:
            key: The key to be added to the cache.
            item: The item to be added to the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = next(iter(self.cache_data))
                print("DISCARD: {}".format(discarded))
                self.cache_data.pop(discarded)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.

        Args:
            key: The key to retrieve from the cache.

        Returns:
            The value associated with the key,
            or None if key is None or doesn't exist.
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
