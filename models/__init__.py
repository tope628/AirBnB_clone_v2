#!/usr/bin/python3
"""
initialize the models package
"""

import os

'''determe which data storage to use'''
if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    print("connection established!")
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
