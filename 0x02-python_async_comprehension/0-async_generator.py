#!/usr/bin/env python3
"""Asynchronous Function ."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """The coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10."""
    for val in range(0, 10):
        asyncio.sleep(1)
        yield float(random.uniform(0, 10))
