#!/usr/bin/env python3
""" Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Implementing put() and get() function """

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item in the cache """

        return self.cache_data.get(key)
