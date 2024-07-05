#!/usr/bin/env python3
""" A type-annotated function. """
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ A type-annotated function. """
    if key in dct:
        return dct[key]
    else:
        return default
