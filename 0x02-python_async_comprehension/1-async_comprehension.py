#!/usr/bin/env python3
"""Creates a list using asynchronous comprehension."""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Gathers a list of values from the async generator and returns it."""
    return [value async for value in async_generator()]
