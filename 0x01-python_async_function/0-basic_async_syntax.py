#!/usr/bin/env python3
"""The basics of async."""
import random
import asyncio


async def wait_random(max_delay=10):
    """an asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that
    waitsfor a random delay between 0 and max_delay (included and
    float value)seconds and eventually returns it."""
    task = float(random.uniform(0, max_delay))
    await asyncio.sleep(task)
    return task
