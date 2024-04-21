#!/usr/bin/python3
'''
__init__ file for models package
'''
from os import getenv


is_db = getenv('HBNB_TYPE_STORAGE') == 'db'

if is_db:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
