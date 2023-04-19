#!/usr/bin/env python3
""" FIFO caching """
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """ Implementing put() and get() function """

    def __init__(self):
        """ Initializing... """
        super().__init__()
        self.queue = deque([])

    def put(self, key, item):
        """ Add an item to the cache """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.queue:
                del_key = self.queue.popleft()
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item in the cache """
        return self.cache_data.get(key)
