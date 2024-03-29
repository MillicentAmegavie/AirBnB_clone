#!/usr/bin/python3
"""Defines amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents amenity.

    Attributes:
        name (str): Name of amenity.
    """

    name = ""
