#!/usr/bin/env python3
""" A type-annotated function. """
from typing import Sequence, Iterable, List, Tuple, Any


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the below function’s parameters and
    return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
