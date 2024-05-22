#!/usr/bin/python3
"""
0-basic_cache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        Assign to dictionary self.cache_data the item value for the key key.
        Args:
            key: The key to be added to the cache.
            item: The item to be added to the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.

        Args:
            key: The key to retrieve from the cache.

        Returns:
            The value associated with the key,
            or None if key is None or doesn't exist.
        """
        return self.cache_data.get(key, None)
