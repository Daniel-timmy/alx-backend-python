#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """ waits for a random delay between 0 and max_delay
    seconds and eventually returns it"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
