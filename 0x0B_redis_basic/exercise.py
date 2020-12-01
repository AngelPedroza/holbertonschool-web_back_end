#!/usr/bin/env python3
""" Module to study Redis and practice """
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


class Cache:
    """ Class to implement cache strategy with redis """

    def __init__(self):
        """ Constructor method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Get a data that will be saved in redis like value of
        a random key that will be created with uuid.
        """
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(
            self,
            key: str,
            fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """Get method. Extract the information saved in redis
        with the key that is passed.
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """ Parameterizes a value from redis to str """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Parameterizes a value from redis to int """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
