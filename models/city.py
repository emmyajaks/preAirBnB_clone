#!/usr/bin/python3
"""
The City Module.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represent a city.

    Attributes are:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""