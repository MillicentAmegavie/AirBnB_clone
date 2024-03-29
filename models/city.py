#!/usr/bin/python3
"""Defines city class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent city.

    Attributes:
        state_id (str): State id.
        name (str): Name of city.
    """

    state_id = ""
    name = ""
