#!/usr/bin/env python3
"""Print info in a collection"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
collention = client.logs.nginx

print(f"{collention.estimated_document_count()} logs")
print("Methods:")
for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    print(f"\tmethod {method}: {collention.count_documents({'method': method})}")
print(collention.count_documents({'path': "/status"}), "status check")
