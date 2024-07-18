#!/usr/bin/python3
"""
redis
"""
import redis
from typing import Union
from uuid import uuid4


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
