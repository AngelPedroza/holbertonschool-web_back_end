#!/usr/bin/env python3
"""returns all students sorted by average score"""


def top_students(mongo_collection):
    """
    All students sorted by average score
    :param mongo_collection: pymongo inyection
    :return: a list with all students filtered
    """
    return mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {'$avg': "$topics.score"}
            }
        },
        {'$sort': {"averageScore": -1}}
    ])
