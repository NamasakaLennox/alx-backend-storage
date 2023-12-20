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
