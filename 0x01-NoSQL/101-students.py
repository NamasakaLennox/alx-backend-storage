#!/usr/bin/env python3
"""
returns all students sorted by average
"""


def top_students(mongo_collection):
    """
    averages all student scores and returns the sorted list
    """
    out = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])

    return out
