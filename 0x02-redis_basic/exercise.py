#!/usr/bin/env python3
"""
redis
"""
import redis
from typing import Union, Callable, Optional
from uuid import uuid4
Utype = Union[str, bytes, int, float]


class Cache:
    """
    define class Cache
    """
    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ def store """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key


def get(self, key: str, fn: Optional[Callable] = None) -> Utype:
    """ def get """
    if fn:
        return fn(self._redis.get(key))
    data = self._redis.get(key)
    return data


def get_int(self: bytes) -> int:
    """get a number"""
    return int.from_bytes(self, sys.byteorder)


def get_str(self: bytes) -> str:
    """get a string"""
    return self.decode("utf-8")
