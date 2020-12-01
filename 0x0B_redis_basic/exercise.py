#!/usr/bin/env python3
""" My cache class module """
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """ My cache class for redis """

    def __init__(self):
        """ Constructor method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Get a data that will be saved in redis like value of
        a random key that will be created with uuid.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
