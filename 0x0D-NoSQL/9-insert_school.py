#!/usr/bin/env python3
""" MongoDB insert python usage """


def insert_school(mongo_collection, **kwargs):
    """Inser in school collection a document"""
    if len(kwargs) == 0:
        return None

    return mongo_collection.insert(kwargs)
