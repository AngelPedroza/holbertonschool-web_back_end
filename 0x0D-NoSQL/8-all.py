#!/usr/bin/env python3

def list_all(mongo_collection):
    """Return all documents"""
    return mongo_collection.find()
