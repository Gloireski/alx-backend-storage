#!/usr/bin/env python3
""" define get_page """
import requests
from typing import Callable
from functools import wraps


def get_page(url: str) -> str:
    """ obtain the HTML content of a particular URL and returns it """
    response = requests.get(url)
    return response.text
