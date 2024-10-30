#!/usr/bin/python3
""" BaseCaching module
"""

from BaseCaching import BaseCaching


class FIFOCache(BaseCaching):
    """
    a class FIFOCache that inherits from BaseCaching and is a caching system:
    """

    def __init__(self) -> None:
        """
        initializer
        """
        super().__init__()
        self.order = [] # create an order to keep track of FIFO keys

    def put(self, key, item) -> None:
        """
        adds new cache items to a cache  system
        :param key: key value of the cache system
        :param item: value if the item
        :return:
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        # Add or update the cache with the new item
        self.cache_data[key] = item
        self.order.append(key)  # Add key to order list

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)  # Remove the oldest key
            del self.cache_data[oldest_key]  # Remove the oldest item from cache
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        returns the cache values
        :param key: values passed
        :return: value in cache data
        """
        return self.cache_data.get(key, None)
