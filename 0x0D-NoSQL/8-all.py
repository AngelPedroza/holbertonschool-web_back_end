#!/usr/bin/env python3
""" MongoDB find python usage"""


def list_all(mongo_collection):
    """Return all documents"""
    return [] if mongo_collection.count() == 0 else mongo_collection.find()
