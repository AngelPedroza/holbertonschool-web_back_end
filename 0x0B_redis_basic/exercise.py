#!/usr/bin/env python3
""" Module to study Redis and practice """
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count how many times a function is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapped(self, *args, **kwargs):
        """EXtra behavior to function that will count"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapped


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs
    for a particular function.
    """

    @wraps(method)
    def wrapped(self, *args, **kwargs):
        """Extra behavior to function that will count"""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapped


class Cache:
    """ Class to implement cache strategy with redis """

    def __init__(self):
        """ Constructor method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
