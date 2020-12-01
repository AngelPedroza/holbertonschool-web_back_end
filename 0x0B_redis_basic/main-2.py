#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(data=b"first")
print(cache.get(cache.store.__qualname__))

cache.store(data=b"second")
cache.store(data=b"third")
print(cache.get(cache.store.__qualname__))