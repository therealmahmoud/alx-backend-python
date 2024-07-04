#!/usr/bin/env python3
""" A type-annotated function. """


def sum_list(input_list: list[float]) -> float:
    """Returns sum of floats in a list."""
    return float(sum(input_list))
