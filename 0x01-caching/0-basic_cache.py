#!/usr/bin/python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    a class BasicCache that inherits from BaseCaching and is a caching system:
    """
    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.

        :param key: dictionary key
        :param item: value
        :return:
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        retrieves a key item
        :param key: cache value pairs
        :return:
        """
        return self.cache_data.get(key, None)
