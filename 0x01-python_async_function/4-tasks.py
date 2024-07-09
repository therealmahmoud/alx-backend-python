#!/usr/bin/env python3
""" Task 4."""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times."""
    tasks = [wait_random(max_delay) for i in range(n)]
    wait_times = await asyncio.gather(*tasks)
    return sorted(wait_times)
