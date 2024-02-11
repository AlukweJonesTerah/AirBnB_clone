#!/usr/bin/python3
"""
This initialization module
initializes packages to create FileStorage instance
to allow the FileStorage class and module to be accessed
by other classes easily
"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
