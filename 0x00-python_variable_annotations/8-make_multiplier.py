#!/usr/bin/env python3
"""type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument and re
    turns a function that multiplies a float by multiplier.
    """
    def mul(multi: float) -> float:
        return multi * multiplier
    return mul
