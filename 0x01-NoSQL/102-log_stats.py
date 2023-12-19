#!/usr/bin/env python3
"""
provides some stats about nginx logs stored in mongoDB
"""
from pymongo import MongoClient


def get_stats():
    """
    gets some stats from nginx logs
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print(f"{nginx.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {nginx.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {nginx.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {nginx.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {nginx.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {nginx.count_documents({'method': 'DELETE'})}")
    query = {"method": "GET", "path": "/status"}
    print(f"{nginx.count_documents(query)} status check")

    ips = nginx.aggregate([
        {
            '$group': {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        },
        {
            "$project": {
                "_id": 0,
                "ip": "$_id",
                "count": 1
            }
        }
    ])
    print("IPs:")
    for ip in ips:
        print(f"\t{ip.get('ip')}: {ip.get('count')}")


if __name__ == "__main__":
    get_stats()
