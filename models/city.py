#!/usr/bin/python3

"""
this a city Module
has a class City that initiates the City
where the AirBnb is
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    This class inherits form the BaseModel class which
    is the parent class

    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new City"""
        super().__init__(*args, **kwargs)
