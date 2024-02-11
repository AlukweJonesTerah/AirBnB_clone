#!/usr/bin/python3

"""
This is state module
this mode inherits the attributes from Basemodel
class from the base model.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This class inherits from the Basemodel class
    """
    name: str = ""
