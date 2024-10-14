#!/usr/bin/env python3
""" The basics of async """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that waits
    for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.

    Argument:
        max_delay (int): maximum delay between two random numbers
    Return:
        float: random number between 0 and max_delay
    """
    time_to_wait = random.uniform(0, max_delay)
    await asyncio.sleep(time_to_wait)
    return time_to_wait
