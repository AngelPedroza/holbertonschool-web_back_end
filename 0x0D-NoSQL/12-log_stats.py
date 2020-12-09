#!/usr/bin/env python3
"""Print info in a collection"""
from pymongo import MongoClient

if __name__ == "__main__":
    """ Make a check for all elements in a collention """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collention = client.logs.nginx

    print(f"{collention.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = collention.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")

    check_get = collention.count_documents({'method': 'GET', 'path': "/status"})
    print(f"{check_get} status check")
