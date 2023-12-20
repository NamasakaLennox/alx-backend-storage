#!/usr/bin/env python3
"""
obtain the HTML content of a particular URL and returns it
"""
import requests
import redis
from functools import wraps

store = redis.Redis()


def cout_access(method):
    """
    decorator to count how many times a url is accessed
    """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        return html
    return wrapper


@count_access
def get_page(url:str) -> str:
    """
    simply returns the html content of a page
    """
    res = requests.get(url)
    return res.text
