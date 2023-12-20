#!/usr/bin/env python3
"""
module for implementing redis in python
"""
import redis
from uuid import uuid4
from typing import Any, Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    counts the number of times a method has been called
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        a wrapper decorator to return the wrapper
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    stores history of inputs and outputs of a function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        a wrapper decorator
        """
        inputs = str(args)
        outputs = str(method(self, *args, *kwargs))
        self._redis.rpush(method.__qualname__ + ":inputs", inputs)
        self._redis.rpush(method.__qualname__ + ":outputs", outputs)

        return outputs
    return wrapper


class Cache:
    """
    A cache store class
    """
    def __init__(self) -> None:
        """
        class constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        takes a data argument and returns a string
        """
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        gets data from store in their desired types
        """
        value = self._redis.get(key)
        if not fn:
            return value
        return fn(value)

    def get_str(self, key: str) -> str:
        """
        parametize get with string
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        add an int parameter
        """
        return self.get(key, int)
