#!/usr/bin/env python3
"""MongoDB aggregate python usage"""


def schools_by_topic(mongo_collection, topic):
    """
    Use an aggregate to find documents
    :param mongo_collection: Pymongo connection
    :param topic: The topic to search
    :return: The list of matchs
    """
    return [i for i in mongo_collection.find({"topic": topic})]

