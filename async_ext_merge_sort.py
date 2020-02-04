#!/usr/bin/env python3

from collections import deque
import math
import os
import sys
import asyncio
import unittest
import logging
logging.basicConfig(level=logging.INFO,
                    filename='err_asy.log',
                    filemode='w',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )


class asymerge():
    def __init__(self):
        super().__init__()

    async def hello(self):
        logging.info("Hello world!")
        r = await asyncio.sleep(1)
        logging.info("Hello again!")


class test_asy(unittest.TestCase):
    def test_init(self):
        pass

    def test_hello(self):
        foo = asymerge()
        loop = asyncio.get_event_loop()
        task = [foo.hello(),foo.hello()]
        loop.run_until_complete(asyncio.wait(task))
        loop.close()
