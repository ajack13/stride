# =============================================================
# Created Date : 19/1/2017
# Name : cache.py
# Contributers : Ajay
# =============================================================

""" 
Caching system for the app
The information is stored in memory ,all data will be lost on server restart
The caching limit can be extended as required
"""
import datetime
class MyCache:
 
    def __init__(self):
        """Constructor"""
        self.cache = {}
        self.max_cache_size = 3
 
    def __contains__(self, key):
        """
        Returns True or False on whether or not the key exists
        """
        print '__contains__'
        return key in self.cache
 
    def update(self, key):
        """
        Update the cache dictionary and optionally remove the oldest item
        """
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            self.remove_oldest()
 
        self.cache[key] = {'date_stored': datetime.datetime.now()}
 
    def remove_oldest(self):
        """
        Remove the entry that has the oldest date
        """
        oldest_entry = None
        for key in self.cache:
            if oldest_entry is None:
                oldest_entry = key
            elif self.cache[key]['date_stored'] < self.cache[oldest_entry]['date_stored']:
                oldest_entry = key
        self.cache.pop(oldest_entry)
