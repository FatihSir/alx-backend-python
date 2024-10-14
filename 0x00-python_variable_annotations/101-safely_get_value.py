#!/usr/bin/env python3
""" safely_get_value Module """


from typing import Union, Any, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, Any] = None) \
        -> Union[T, Any]:
    """The function is intended to be used to practice duck-typed annotation"""
    if key in dct:
        return dct[key]
    else:
        return default
