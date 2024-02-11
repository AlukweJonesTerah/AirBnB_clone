#!/usr/bin/python3

"""
amenity model
this model inherits from the Parent class BaseModel
these are basic items that a guest expects in order
to have a comfortable stay. These include:

Toilet paper
Soap (for hands and body)
One towel per guest
One pillow per guest
Linens for each guest bed
"""

from models import base_model


class Amenity(base_model.BaseModel):
    """
    This class inherits from the Base parent class
    This class handles the basic items that guests
    expect
    """
    name: str = ""
