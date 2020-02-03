#!/usr/bin/env python3
import logging
import unittest
import os
import sys
import os
import sys
import unittest
import logging
logging.basicConfig(level=logging.INFO,
                    filename='err.log',
                    filemode='w',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )
'''
The external merge sort module
'''

# merge sort class, accept the maximun size and the list of filenames to make merge sort, also offer a static version of merge sort


class mergesort:

    # constructor
    def __init__(self, size, files):
        super().__init__()
        self._size = 0
        self._files = files

    # read a single unsorted file and output sorted
    def readone(self, file):
        pass

    # read multiple unsorted files and output sorted
    def readn(self):
        for each in self._files:
            readone(each)

    # merge sorted files and output multiple
    def mergen(self):
        pass

    # merge sorted files and output single
    def mergeone(self):
        pass

    def sort(self, us):
        if not us or len(us) <= 1:
            return us
        L, R = self.divide(us)
        return self.merge(self.sort(L), self.sort(R))

    # helper dividing function
    def divide(self, us):
        if not us or len(us) <= 1:
            raise ValueError
        # divide into left and right and return
        mid = len(us)//2
        L = us[:mid]
        R = us[mid:]
        return L, R

    # helper mergering function
    def merge(self, l, r):
        # compare from left to right on two list and combine
        logging.info("Current merging:")
        logging.info('l = %s', str(l))
        logging.info('r = %s', str(r))
        i, j = 0, 0
        m, n = len(l), len(r)
        comb = []
        while i < m and j < n:
            if l[i] <= r[j]:
                comb.append(l[i])
                i += 1
            else:
                comb.append(r[j])
                j += 1
        if i < m:
            comb += l[i:]
        elif j < n:
            comb += r[j:]
        return comb

# unit test class


class testMerge(unittest.TestCase):

    def test_init(self):
        pass

    def test_readone(self):
        pass

    def test_readn(self):
        pass

    def test_mergen(self):
        pass

    def test_mergeone(self):
        pass

    def test_sort(self):
        foo = mergesort(10, './')
        self.assertEqual([i for i in range(1, 11)],
                         foo.sort([i for i in range(10, 0, -1)]))

    def test_divide(self):
        foo = mergesort(10, './')
        with self.assertRaises(ValueError):
            cb = foo.divide([])
        with self.assertRaises(ValueError):
            cb = foo.divide([1])
        self.assertEqual(([1], [2]), foo.divide([1, 2]))
        self.assertEqual(([1], [2, 3]), foo.divide([1, 2, 3]))

    def test_merge(self):
        foo = mergesort(10, './')
        self.assertEqual([], foo.merge([], []))
        self.assertEqual([1, 2], foo.merge([2], [1]))
        self.assertEqual([1, 2, 3, 4], foo.merge([2, 3], [1, 4]))
        self.assertEqual([1, 2, 3, 4, 5], foo.merge([1, 2, 3, 4], [5]))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) == 2:
        pass
    else:
        raise ValueError
