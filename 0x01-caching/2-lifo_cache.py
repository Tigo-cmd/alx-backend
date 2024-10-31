#!/usr/bin/python3
"""BaseCaching module documentations
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    a class that inherits from BaseCaching
    """

    def __init__(self):
        """
        initializer
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        handles item addition in a cache stack
        :param key: container
        :param item:
        :return:
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        utilizes the get method.
        """
        return self.cache_data.get(key, None)
