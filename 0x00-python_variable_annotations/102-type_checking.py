#!/usr/bin/env python3
""" zoom_array Module """


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """The function is intended to be used to practice duck-typed annotation"""
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in
