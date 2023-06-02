#!/usr/bin/env python3
"""a coroutine that takes no arguments."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loop 10 times, each time
    asynchronously wait 1 second, then yield a
    random number between 0 and 10. """
    for i in range(10):
        await asyncio.sleep(1)
        result = random.uniform(0, 10)
        yield result
