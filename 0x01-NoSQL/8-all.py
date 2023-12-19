#!/usr/bin/env python3
"""
 lists all documents in a collection:
"""


def list_all(mongo_collection):
    """
    function lists all documents in collection
    """
    return mongo_collection.find({})
