#!/usr/bin/env python3
"""Defines an asynchronous generator that yields random floats."""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields a random float between 0 and 10, after waiting for 1 second."""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
