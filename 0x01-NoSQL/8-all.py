#!/usr/bin/env python3
""" define function list_all """
from typing import List


def list_all(mongo_collection):
    """ function that lists all documents in a collection """
    ls = mongo_collection.find()
    return ls
