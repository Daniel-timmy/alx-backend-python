#!/usr/bin/env python3
"""takes in 2 int arguments (in this order): n and max_delay"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)."""
    mList = []
    dList = []
    for i in range(n):
        val = wait_random(max_delay)
        mList.append(val)

    for task in asyncio.as_completed((mList)):
        delay = await task
        dList.append(delay)

    return sorted(dList)
