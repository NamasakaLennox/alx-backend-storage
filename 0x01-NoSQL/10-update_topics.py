#!/usr/bin/env python3
"""
changes all topics of a school document based on the name
"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]):
    """
    changes topics based on given value
    """
    find = {"name": name}
    new = {"$set": {"topics": topics}}

    updated = mongo_collection.update_one(find, new)
