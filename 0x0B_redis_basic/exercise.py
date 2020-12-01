#!/usr/bin/env python3
"""My cache class module
"""
from redis import Redis
from uuid import uuid4
from typing import Union


class Cache:
    def __init__(self):
        """Construntor method
        """
        self._redis = Redis()
        self._redis.flushdb()

    def stores(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
