#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 上午9:12
# @Author  : chenyuelong
# @Mail    : yuelong_chen@yahoo.com
# @File    : biodata.py
# @Software: PyCharm

import os, sys
import abc
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))

class biodata(metaclass=abc.ABCMeta):
    '''
    data base for biology
    Extend to fastq
    '''

    def __init__(self):
        pass

    @abc.abstractmethod
    def getIndex(self):
        '''
        生成index
        :return:
        '''
        pass


def main():
    pass


if __name__ == '__main__':
    main()