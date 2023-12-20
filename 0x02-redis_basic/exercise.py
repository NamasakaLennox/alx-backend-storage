#!/usr/bin/env python3
"""
module for implementing redis in python
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """
    A cache store class
    """
    def __init__(self):
        """
        class constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        takes a data argument and returns a string
        """
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key, fn=None):
        """
        gets data from store in their desired types
        """
        value = self._redis.get(key)
        if not fn:
            return value
        return fn(value)

    def get_str(self, key):
        """
        parametize get with string
        """
        fn = lambda d: d.decode("utf-8")
        return self.get(key, fn)

    def get_int(self, key):
        """
        add an int parameter
        """

        return self.get(key, int)
