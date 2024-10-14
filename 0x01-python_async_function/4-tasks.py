#!/usr/bin/env python3
"""Module to execute multiple coroutines concurrently using async."""


from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Initiates and runs task_wait_random n times concurrently with
    a maximum delay.

    Args:
        n (int): The number of times to run task_wait_random.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        List[float]: A list of delay values in the order of completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_tasks = asyncio.as_completed(tasks)
    results = [await task for task in completed_tasks]
    return results
