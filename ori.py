#!/usr/bin/env python3

'''
The external merge sort module
'''
import sys
import os
import unittest
import logging
logging.basicConfig(level=logging.INFO,
                    filename='err.log',
                    filemode='w',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )


class mergesort:

    # the constructor store the outer unsorted list
    def __init__(self, unsort):
        super().__init__()
        self.nums = unsort
        self.path = "output/"

    # divide the list into two parts
    def divide(self, us):
        if not us or len(us) <= 1:
            raise ValueError
        # divide into left and right and return
        mid = len(us)//2
        L = us[:mid]
        R = us[mid:]
        return L, R

    # merge two sorted list by two pointers
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

    # merge multiple sorted
    def mergeall(self, us):
        logging.info('us = %s', str(us))
        if not us:
            return us
        elif len(us) == 1:
            return us[0]
        elif len(us) == 2:
            return self.merge(us[0], us[1])
        else:
            n = len(us)
            return self.merge(self.mergeall(us[:n//2]), self.mergeall(us[n//2:]))

    # recursive way of sorting
    def sort(self, us):
        if len(us) <= 1:
            return us
        L, R = self.divide(us)
        return self.merge(self.sort(L), self.sort(R))

    def solve(self):
        self.nums = self.sort(self.nums)
        return self.nums

    # static version
    @staticmethod
    def sortout(unsort):
        return mergesort(unsort).solve()

    # read from path
    def read(self, path):
        filename = path.split("_")[-1]
        self.path += "sorted_"+filename
        unsort = []
        with open(path, 'r') as f:
            for line in f:
                unsort.append(int(line))
        self.nums = unsort
        return unsort

    # read from a path and return sorted
    def readandsort(self, path):
        sub = []
        with open('input/'+path, 'r') as f:
            for line in f:
                sub.append(int(line))
        return mergesort(sub).solve()

    # write to path
    def write(self):
        with open(self.path, 'w') as f:
            for each in self.nums:
                f.write(str(each))
                f.write('\n')

    # method to sort all together
    def sortall(self):
        for file in os.listdir('input/'):
            self.nums.append(self.readandsort(file))
        ans = self.mergeall(self.nums)
        with open('output/sorted.txt', 'w') as f:
            for each in ans:
                f.write(str(each))
                f.write('\n')


# unit tests
class TestMerge(unittest.TestCase):

    # test the sorting function
    def test_init(self):
        foo = mergesort([i for i in range(10, 0, -1)])
        self.assertEqual([i for i in range(1, 11)], foo.solve())

    # test the divide function
    def test_divide(self):
        foo = mergesort([])
        with self.assertRaises(ValueError):
            cb = foo.divide([])
        with self.assertRaises(ValueError):
            cb = foo.divide([1])
        self.assertEqual(([1], [2]), foo.divide([1, 2]))
        self.assertEqual(([1], [2, 3]), foo.divide([1, 2, 3]))

    # test the merget function
    def test_merge(self):
        foo = mergesort([])
        self.assertEqual([], foo.merge([], []))
        self.assertEqual([1, 2], foo.merge([2], [1]))
        self.assertEqual([1, 2, 3, 4], foo.merge([2, 3], [1, 4]))
        self.assertEqual([1, 2, 3, 4, 5], foo.merge([1, 2, 3, 4], [5]))

    # test the static sorting
    def test_st(self):
        self.assertEqual([i for i in range(1, 11)],
                         mergesort.sortout([i for i in range(10, 0, -1)]))

    # test read file
    def test_read(self):
        self.assertEqual([7, 9, 5, 0, 1, 4, 8, 6, 2, 3],
                         mergesort([]).read('data_1.txt'))

    # test merge all
    def test_mergeall(self):
        self.assertEqual([i for i in range(12)], mergesort([]).mergeall(
            [[i for i in range(x, x+3)] for x in range(0, 10, 3)]))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        foo = mergesort([])
        foo.sortall()
        # ans = foo.readandsort('unsorted_1.txt')
        # with open('output/sorted.txt', 'w') as f:
        #     for each in ans:
        #         f.write(str(each))
        #         f.write('\n')
    elif len(sys.argv) == 2:
        foo = mergesort([])
        foo.read(sys.argv[1])
        foo.solve()
        foo.write()
