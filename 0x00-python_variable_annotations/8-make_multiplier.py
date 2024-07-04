#!/usr/bin/env python3
""" A type-annotated function. """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function which multiply two floats."""
    return lambda h: multiplier * h
