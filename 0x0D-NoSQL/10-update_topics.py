#!/usr/bin/env python3
""" MongBD update python usage """


def update_topics(mongo_collection, name, topics):
    """Update a document by name with the topics
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
