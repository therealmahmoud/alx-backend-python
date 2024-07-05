#!/usr/bin/env python3
""" A type-annotated function. """
from typing import Sequence


def element_length(lst: Sequence[int]):
    return [(i, len(i)) for i in lst]
