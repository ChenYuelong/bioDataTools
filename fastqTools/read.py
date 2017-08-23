#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 下午12:54
# @Author  : chenyuelong
# @Mail    : yuelong_chen@yahoo.com
# @File    : read.py
# @Software: PyCharm

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))

class read():
    '''
    fastq中每条read
    '''

    def __init__(self,*args):
        self._readID = args[0]
        self._readseq = args[1]
        self._readinfo = args[2]
        self._readq = args[3]



def main():
    pass


if __name__ == '__main__':
    main()