#!/usr/bin/env python3
""" Multiple coroutines """


import asyncio
import time
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    async routine called wait_n that takes in 2 int arguments (in this order):
    n and max_delay. You will spawn wait_random n times with the
    specified max_delay.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
