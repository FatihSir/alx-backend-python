#!/usr/bin/env python3
""" Measure the runtime """


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
        Spawns wait_random n times with a specified max_delay,
        returns the list of delays in the order they are completed.

        Args:
            n (int): Number of times to run wait_random
            max_delay (int): Maximum delay to pass to wait_random

        Returns:
            float: Delays in the order of completion
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
