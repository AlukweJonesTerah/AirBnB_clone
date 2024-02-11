#!/usr/bin/python3

"""
This is user module
this mode inherits the attributes from Basemodel
class from the base model.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class inherits from the Basemodel class
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
