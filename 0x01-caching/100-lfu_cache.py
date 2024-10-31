#!/usr/bin/python3
""" BaseCaching module
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    An object for storing and retrieving items with an
    LFU removal policy when the limit is reached.
    """
    def __init__(self):
        """
        Initializer.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """
        Updates the cache order to prioritize the most recently used item.
        """
        max_pos = []
        frequency = 0
        position = 0
        initial = 0
        for i, key_fr in enumerate(self.keys_freq):
            if key_fr[0] == mru_key:
                frequency = key_fr[1] + 1
                position = i
                break
            elif len(max_pos) == 0:
                max_pos.append(i)
            elif key_fr[1] < self.keys_freq[max_pos[-1]][1]:
                max_pos.append(i)
        max_pos.reverse()
        for pos in max_pos:
            if self.keys_freq[pos][1] > frequency:
                break
            initial = pos
        self.keys_freq.pop(position)
        self.keys_freq.insert(initial, [mru_key, frequency])

    def put(self, key, item):
        """
        handles item addition in a cache stack
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """
        Retrieves an item by key from a cache system
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
