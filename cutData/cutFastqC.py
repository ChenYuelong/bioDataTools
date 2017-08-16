#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/8/16 下午3:52
# @Author  : chenyuelong
# @Mail    : yuelong_chen@yahoo.com
# @File    : cutFastqC.py
# @Software: PyCharm

import os, sys
import subprocess
import numpy as np
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))


class cutfastqC():
    '''
    trim fastq data(use c program fastq-tool)
    '''

    def __init__(self, *fastq, length=0, size=0, outprefix=''):
        self._file = fastq
        self._fastq = []
        self._length = float(length)
        self._size = self._normalized(size)
        self._out = outprefix
        self._fs = '/annoroad/data1/bioinfo/PROJECT/RD/Medical/Leukemia/chenyl/bin/fastq-sample'
        self._gzip = '/bin/gzip'
        self._gunzip = '/bin/gunzip'
        self._tmp = []

    def _normalized(self, size):
        return float(size) * 1000000000

    @property
    def _readcount(self):
        count = int(self._size / (self._length*len(self._file)))
        return count

    def _Popen(self,cmd):
        p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        return p

    def _getcmd(self):
        cmd = '{0} -n {1} -s 422 -o {2}'.format(self._fs,self._readcount,self._out)
        for i in self._fastq:
            cmd = '{0} {1}'.format(cmd,i)
        return cmd

    def _gunzipf(self,file):
        tmp = '{0}.{1}.fastq'.format(self._out,np.random.randint(1000))
        self._tmp.append(tmp)
        self._fastq.append(tmp)
        cmd = '{0} -c {1} > {2}'.format(self._gunzip,file,tmp)
        return cmd

    def _gzipf(self,file):
        cmd = '{0} {1}'.format(self._gzip,file)
        return cmd

    def _read(self):
        pSet =[]
        for file in self._file:
            if '.gz' in os.path.basename(file):
                cmd =self._gunzipf(file)
                pSet.append(self._Popen(cmd))
            else:
                self._fastq.append(file)
        while len(pSet) > 0:
            p = pSet.pop()
            print(p.communicate())

    def _write(self):
        pSet = []
        if len(self._fastq) == 1:
            cmd = self._gzipf('{}.fastq'.format(self._out))
            pSet.append(self._Popen(cmd))
        else:
            for i in range(1,len(self._fastq)+1):
                cmd = self._gzipf('{0}.{1}.fastq'.format(self._out,i))
                pSet.append(self._Popen(cmd))
        while len(pSet) > 0:
            p = pSet.pop()
            print(p.communicate())
        print('gzip finished!')

    def _remove(self):
        for file in self._tmp:
            cmd = 'rm {}'.format(file)
            print(self._Popen(cmd).communicate())
        print('Remove tmp files')

    def run(self):
        self._read()
        p = self._Popen(self._getcmd())
        print(p.communicate())
        self._remove()
        self._write()





def main():
    pass


if __name__ == '__main__':
    main()