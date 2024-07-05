#!/usr/bin/env python3
""" A type-annotated function. """
from typing import Any, Sequence, Union, TypeVar


NoneType = TypeVar("NoneType")
def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    if lst:
        return lst[0]
    else:
        return None
