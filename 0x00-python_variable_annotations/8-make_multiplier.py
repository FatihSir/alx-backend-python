#!/usr/bin/env python3
""" make_multiplier Module """


from typing import Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A function that takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier.

    Arguments:
        multiplier (float): a float to be multiplied.
    Return:
        a function that multiplies a float by multiplier.
    """

    return lambda n: n * multiplier
