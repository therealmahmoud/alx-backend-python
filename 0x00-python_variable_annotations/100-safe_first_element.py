#!/usr/bin/env python3
""" A type-annotated function. """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ A type-annotated function. """
    if lst:
        return lst[0]
    else:
        return None
