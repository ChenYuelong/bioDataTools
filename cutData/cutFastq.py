#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/8/16 下午1:26
# @Author  : chenyuelong
# @Mail    : yuelong_chen@yahoo.com
# @File    : cutFastq.py
# @Software: PyCharm

import os, sys
import gzip

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))


class cutfastq():
    '''
    trim fastq data
    虽说可以完成这个功能，但是速度太慢了。
    '''

    def __init__(self, fastq, length, size, out):
        self._fastq = fastq
        self._length = float(length)
        self._size = self._normalized(size)
        self._out = out

    def _normalized(self, size):
        return float(size) * 1000000000

    @property
    def _readcount(self):
        count = int(self._size / self._length)
        return count

    def _read(self):
        filename = os.path.basename(self._fastq)
        if '.gz' in filename:
            f = self._gzipread()
        else:
            f = self._fastqread()
        return f

    def _fastqread(self):
        f = open(self._fastq, 'r')
        return f

    def _gzipread(self):
        f = gzip.open(self._fastq, 'rb')
        return f

    def _gzipwriter(self):
        wf = gzip.open(self._out, 'wb')
        return wf

    def _fastqwriter(self):
        wf = open(self._out, 'w')
        return wf

    def _writer(self):
        filename = os.path.basename(self._out)
        if '.gz' in filename:
            wf = self._gzipwriter()
        else:
            wf = self._fastqwriter()
        return wf

    def run(self):
        with self._read() as rf , self._writer() as wf:
            line = 0
            while line  < self._readcount * 4:
                line = line + 1
                rline = rf.read()
                wf.write(rline)


def main():
    pass


if __name__ == '__main__':
    main()
