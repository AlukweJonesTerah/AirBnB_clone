#!/usr/bin/python3

"""
This is review module
this mode inherits the attributes from Basemodel
class from the base model.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class inherits from the Basemodel class
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a Review object"""
        super().__init__(*args, **kwargs)
