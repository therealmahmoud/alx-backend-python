#!/usr/bin/env python3
""" A type-annotated function. """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns sum of floats in a list."""
    return float(sum(input_list))
