#!/usr/bin/env python3
""" make_multiplier Module """


from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """The function is intended to be used to practice duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None
