#!/usr/bin/env python3
"""
redis
"""
import redis
from typing import Union, Callable, Optional, Any
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


def get(self, key: str, fn: Optional[Callable] = None) -> Any:
    """
    convert the data back
    to the desired format
    :param key:
    :param fn:
    :return:
    """
    client = self._redis
    value = client.get(key)
    if not value:
        return
    if fn is int:
        return self.get_int(value)
    if fn is str:
        return self.get_str(value)
    if callable(fn):
        return fn(value)
    return value


def get_int(self: bytes) -> int:
    """get a number"""
    return int.from_bytes(self, sys.byteorder)


def get_str(self: bytes) -> str:
    """get a string"""
    return self.decode("utf-8")
