#!/usr/bin/env python3

from collections import deque
import math
import os
import sys
import asyncio
import unittest
import logging
logging.basicConfig(level=logging.WARNING,
                    filename='err_asy.log',
                    filemode='w',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )


class inbuff:
    def __init__(self, infile):
        super().__init__()
        self.file = infile
        self.buff = deque()
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
        return list(self.buff)

    def peek(self):
        if not self.buff:
            return None
        return self.buff[0]

    def pop(self):
        if not self.buff:
            return None
        return self.buff.popleft()


class outbuff:
    def __init__(self, size):
        super().__init__()
        self.buff = []
        self.size = size

    def push(self, v):
        logging.info("Now pushing %d" % v)
        self.buff.append(v)
        if len(self.buff) >= self.size:
            self.out()
        logging.info("Buff after push is %s" % str(self.buff))

    def out(self):
        with open('output/sorted.txt', 'a') as f:
            for each in self.buff:
                f.write(str(each)+'\n')
        self.buff.clear()


class asymerge():
    def __init__(self):
        super().__init__()
        self.inbuffs = []
        self.outbuff = outbuff(10)

    async def sortOne(self, file):
        name = file.split('_')[-1]
        logging.info("Current name is %s" % name)
        st = []
        with open('input/'+file, 'r') as f:
            for line in f:
                st.append(int(line))
        st.sort()
        with open('tmp/tmp_'+name, 'w') as f:
            for each in st:
                f.write(str(each) + '\n')

    async def sort(self, files):
        tasks = [self.sortOne(file) for file in files]
        await asyncio.wait(tasks)

    def merge(self, files):
        for each in files:
            self.inbuffs.append(inbuff('tmp/'+each))
            self.inbuffs[-1].read(9)
            logging.info("The initial inbuff of %s is %s" %
                         (each, str(self.inbuffs[-1].buff)))
        while True:
            m = math.inf
            ind = -1
            empty = 0
            logging.info("Now start to finding minimum")
            for i, v in enumerate(self.inbuffs):
                if v.peek() == None:
                    v.read(9)
                    if v.peek() == None:
                        empty += 1
                        continue
                if v.peek() < m:
                    ind = i
                    m = v.peek()
            logging.info("Now the empty is %d" % empty)
            if empty == 10:
                self.outbuff.out()
                break

            logging.info("Found %d from %dth buff is smallest" %
                         (self.inbuffs[ind].peek(), ind))
            m = self.inbuffs[ind].pop()
            if not self.inbuffs[ind].peek:
                logging.info("Now the %dth buff is empty" % ind)
                self.inbuffs[ind].read(9)
            self.outbuff.push(m)


if __name__ == '__main__':
    foo = asymerge()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(foo.sort(os.listdir('input')))
    finally:
        loop.close()
    foo.merge(os.listdir('tmp'))
