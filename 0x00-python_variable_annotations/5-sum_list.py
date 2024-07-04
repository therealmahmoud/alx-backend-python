#!/usr/bin/env python3
""" A type-annotated function. """


def sum_list(input_list: list[float]) -> float:
    s: float = 0
    for i in range(len(input_list)):
        s += input_list[i]
    return s
