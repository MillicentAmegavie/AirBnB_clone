#!/usr/bin/python3
"""Defines state class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent state.

    Attributes:
        name (str): Name of the state.
    """

    name = ""
