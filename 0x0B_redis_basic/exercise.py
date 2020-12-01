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
        """Set data with a uuid key directly in redis
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
