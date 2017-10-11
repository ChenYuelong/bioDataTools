#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/9/27 16:37
# @Author  : chenyuelong
# @Mail    : yuelong_chen@yahoo.com
# @File    : time_test.py
# @Software: PyCharm

import os, sys
import time
import gzip
import subprocess
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))

'''
这个程序用来测试速度

1. 利用gzip包来遍历一遍gz文件的时间
2. 利用subprocess来先进行解压，解压后遍历一边文件，在subprocess进行压缩

'''

def gzipRead(file):
    start = time.time()
    with gzip.GzipFile(file,'rb') as f:
        for i in f.readlines():
            pass
    print(i)
    end = time.time()
    print('gzip:{}'.format(end-start))

def subprocessRead(file):
    start = time.time()
    cmd = 'gunzip {}'.format(file)
    p = subprocess.Popen(cmd,shell=True)
    p.communicate()
    gunzipfile = file.replace('.gz','')
    with open(gunzipfile,'r') as f:
        for i in f.readlines():
            pass
    print(i)
    cmd = 'gunzip {}'.format(gunzipfile)
    p = subprocess.Popen(cmd,shell=True)
    p.communicate()
    end = time.time()
    print('subprocess:{}'.format(end - start))





def main():
    file = '/annoroad/data1/bioinfo/PROJECT/RD/Medical/Leukemia/V2_panel/test12_RERUN_20160120/chenyuelong/tmp/test.fq.gz'
    gzipRead(file)
    subprocessRead(file)



if __name__ == '__main__':
    main()