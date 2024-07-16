#!/usr/bin/env python3
""" define function insert_school """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs """
    # print(kwargs.get('address'))
    ls = mongo_collection.insert_one(kwargs)
    return ls.inserted_id
