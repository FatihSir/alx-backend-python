#!/usr/bin/env python3
""" make_multiplier Module """


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:

    """
    A function that takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier.

    Arguments:
        lst (Iterable[Sequence]): a list of sequence (list, set, string)
    Return:
        list of tuple that contains the length of each element in the list.
    """
    return [(i, len(i)) for i in lst]
