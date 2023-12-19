#!/usr/bin/env python3
"""
returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    takes a topic and returns a list of school having that topic
    """
    a = mongo_collection.find({"topics": {"$in": [topic]}})
    return a
