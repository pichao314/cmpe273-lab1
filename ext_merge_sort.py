#!/usr/bin/env python3

import os
import sys
import unittest
import logging
logging.basicConfig(level=logging.INFO,
                    filename='err.log',
                    filemode='w',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )

# input and output buffer


class inbuff:
    def __init__(self, infile):
        super().__init__()
        self.file = infile
        self.buff = []
        self.loc = 0

    def read(self, size):
        with open(self.file, 'r') as f:
            self.buff.clear()
            start = self.loc
            self.loc += size
            end = start + size
            logging.info("Current fetching from %d to %d" % (start, end))
            for i, v in enumerate(f):
                if i >= start and i < end and v:
                    self.buff.append(int(v))
            logging.info("Fetching result is %s" % str(self.buff))
        return self.buff


class outbuff:
    def __init__(self, size):
        super().__init__()
        self.buff = []
        self.size = size

    def push(self, v):
        logging.info("Now pushing %d" % v)
        self.buff.append(v)
        if len(self.buff) >= self.size:
            with open('output/sorted.txt', 'a') as f:
                for each in self.buff:
                    f.write(str(each)+'\n')
            self.buff.clear()
        logging.info("Buff after push is %s" % str(self.buff))
# unit test class


class testMerge(unittest.TestCase):
    def test_init(self):
        pass

    def test_inbuff(self):
        foo = inbuff("intest.txt")
        self.assertEqual([i for i in range(10)], foo.read(10))
        self.assertEqual([i for i in range(10, 20)], foo.read(10))
        self.assertEqual([], foo.read(1))

    def test_outbuff(self):
        foo = outbuff(10)
        for i in range(9):
            foo.push(i)
            self.assertEqual([j for j in range(i+1)], foo.buff)
        foo.push(9)
        self.assertEqual([], foo.buff)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) == 2:
        pass
    else:
        raise ValueError
