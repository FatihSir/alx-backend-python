#!/usr/bin/env python3
""" string and int/float to tuple Module """


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """
    A function that takes a string k and an int OR float v as arguments
    and returns a tuple. The first element of the tuple is the string k.
    The second element is the square of the int/float v

    Arguments:
        k (str): a string
        v (Union[int, float]): an integer or float
    Return:
        Tuple of the first element and the square of the second element
    """
    return k, v ** 2
