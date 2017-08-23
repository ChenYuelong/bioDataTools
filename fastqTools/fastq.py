#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 上午9:09
# @Author  : chenyuelong
# @Mail    : yuelong_chen@yahoo.com
# @File    : fastq_str.py
# @Software: PyCharm

import os, sys
import gzip
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))
from biodata import biodata


class fastq(biodata):
    '''
    fastq数据类
    '''

    def __init__(self, fastq):
        biodata.__init__(self)
        self._fastq = fastq
        self._idx = []
        self._idxf = '{}.fqidx'.format(self._fastq)

    def _readindex(self):
        '''
        读取index文件
        :return: index列表
        '''
        with open(self._idxf, 'r') as f:
            idx = []
            for line in f.readlines():
                idx.append(line.strip('\n'))
        return idx

    def _readfastq(self):
        suffix = os.path.splitext(self._fastq)[1]
        if suffix == '.fastq' or suffix == '.fq':
            fbuffer = open(self._fastq, 'r')
            return fbuffer
        elif suffix == '.gz':
            fbuffer = gzip.GzipFile(self._fastq,'rb')
            return fbuffer
        else:
            raise TypeError('FASTQ file must be .fastq or .fq or .gz')

    def getIndex(self):
        if os.path.exists(self._idxf):
            self._idx = self._readindex()
            # self._idx.reverse()
            return True
        else:
            with self._readfastq() as fbuff, open(self._idxf, 'w') as f:
                start = str(fbuff.tell())

                linenumber = 0
                while 1:
                    linenumber += 1
                    line = fbuff.readline()
                    if not line:
                        # if linenumber > 1:
                        # self._idx.append(start)
                        # self._idx.reverse()
                        # f.write('{}\n'.format(start))
                        break
                    if linenumber == 400:
                        self._idx.append(start)
                        f.write('{}\n'.format(start))
                        start = str(fbuff.tell())
                        linenumber = 0
        return True

    def sample(self, n, seed=''):
        return self._sample(n, seed)

    def _sample(self, n=100000, seed=''):
        '''
        从fastq数据中抽取一定量的read
        :param n: 抽样的read数
        :param seed: 随机种子，默认为422
        :return: 抽样列表
        '''
        if seed != '':
            random.seed(int(seed))
        samplelist = []
        with self._readfastq() as rfq:
            if n < len(self._idx):
                choose = random.sample(self._idx, n)
                samplelist = self._getRead(rfq, choose)
            elif 100 * len(self._idx) > n > len(self._idx):
                average = int(n / len(self._idx))
                anothern = int(n % len(self._idx))
                samplelist = self._getRead(rfq, self._idx, average, anothern)
            else:
                raise ValueError('Sample size was large than source!')
        print('sample size:{}'.format(len(samplelist) / 4))
        return samplelist

    def _getRead(self, fqbuffer, idxes, aver=1, more=0):
        sl = []
        for i in idxes:
            if more > 0:
                lines = (aver + 1) * 4
                more = more - 1
            else:
                lines = aver * 4
            fqbuffer.seek(int(i))
            for j in range(lines):
                if isinstance(fqbuffer,gzip.GzipFile):
                    sl.append(bytes.decode(fqbuffer.readline()).strip('\n'))
                else:
                    sl.append(fqbuffer.readline().strip('\n'))
        return sl

    def run(self):
        self.getIndex()
        # print(self.sample(5))
        # random.seed(1)
        # choose = random.sample(self._idx, 50000)
        # print(choose)
        # with self._readfastq() as mytest:
        #     for i in choose:
        #         mytest.seek(int(i[0]))
        #         for j in range(4):
        #             pass
        # print(mytest.readline().strip('\n'))
        # print(i)


def main():
    test = fastq(
        '/annoroad/data1/bioinfo/PROJECT/RD/Medical/Leukemia/V2_panel/test12_RERUN_20160120/chenyuelong/tmp/test20000.fq.gz')
    # test.getIndex()
    test.test()


if __name__ == '__main__':
    main()
