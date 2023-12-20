#!/usr/bin/env python3
"""
obtain the HTML content of a particular URL and returns it
"""
import requests
import redis
from typing import Callable
from functools import wraps

store = redis.Redis()


def cout_access(method: Callable) -> Callable:
    """
    decorator to count how many times a url is accessed
    """
    @wraps(method)
    def wrapper(url) -> str:
        """
        wrapper function for caching
        """
        store.incr(f'count:{url}')
        result = store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')

        result = method(url)
        store.set(f'count:{url}', 0)
        store.setex(f'result:{url}', 10, result)
        return result

    return wrapper


@count_access
def get_page(url:str) -> str:
    """
    simply returns the html content of a page
    """
    res = requests.get(url)
    return res.text
