#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay=10) -> float:
    """ waits for a random delay between 0 and max_delay
    seconds and eventually returns it"""
    i = random.random() * max_delay
    await asyncio.sleep(i)
    return i
