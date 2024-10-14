#!/usr/bin/env python3
""" Multiple coroutines """


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs wait_random asynchronously n times with a specified max_delay and
    returns the list of completed delays in the order they finish.

    Args:
        n (int): The number of times to run wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of delays, sorted in the order of completion.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
