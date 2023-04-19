#!/usr/bin/env python3
""" LRU Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Implementing put() and get() function """

    def __init__(self):
        """ Initializing... """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Get an item in the cache """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.keys:
                del_key = self.keys.pop(0)
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))
            if key in self.keys:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ Get an item using key """
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key)
