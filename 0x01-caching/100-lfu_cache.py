#!/usr/bin/python3
"""
100-lfu_cache module
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialize the class and call the parent init method
        """
        super().__init__()
        self.cache_data = {}
        self.frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """
        Assign to dictionary self.cache_data the item value for the key key.

        Args:
            key: The key to be added to the cache.
            item: The item to be added to the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
                self.usage_order.move_to_end(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lfu_keys = [k for k, v in self.frequency.items()
                                if v == min(self.frequency.values())]
                    if len(lfu_keys) > 1:
                        lfu_key = next(k for k in self.usage_order
                                       if k in lfu_keys)
                    else:
                        lfu_key = lfu_keys[0]

                    print("DISCARD: {}".format(lfu_key))
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]
                    del self.usage_order[lfu_key]

                self.cache_data[key] = item
                self.frequency[key] = 1
                self.usage_order[key] = None

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.

        Args:
            key: The key to retrieve from the cache.

        Returns:
            The value associated with the key,
            or None if key is None or doesn't exist.
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
            return self.cache_data[key]
        return None
