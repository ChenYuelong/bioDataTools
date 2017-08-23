#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 下午4:41
# @Author  : chenyuelong
# @Mail    : yuelong_chen@yahoo.com
# @File    : fastqSample.py
# @Software: PyCharm

import os, sys
import argparse
import gzip
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))
from fastqTools.fastq import fastq

def main():
    parser = argparse.ArgumentParser(description='fastq抽样程序:\n'
                                                 '第一次运行会速度较慢，但是运行后会生成fqidx文件，再次进行抽样时速度'
                                                 '速度加快')
    parser.add_argument('--fastq','-f',dest='fastq',action='store',
                        help='fastq files(must), suffix must be .fq or .fastq'
                             'if in a gzip, suffix must be .gz',
                        default='')
    parser.add_argument('--sample','-s',dest='n',action='store',
                        help='sample Number(optional,default=10000)',
                        default=10000)
    parser.add_argument('--seed','-seed',dest='seed',action='store',
                        help='random seed(optional,default=null)',
                        default='')
    parser.add_argument('--output','-o',dest='output',action='store',
                        help='output(must),if wants store results in gzip,suffix must be .gz',
                        default='')
    args = parser.parse_args()

    if args.fastq == '' or args.output == '':
        parser.print_help()
        sys.exit(1)
    else:
        sampleFq = fastq(args.fastq)
        sampleFq.run()
        print(int(args.n))
        samplelist = sampleFq.sample(int(args.n),args.seed)

        with getWriteBuff(args.output) as f:
            if isinstance(f,gzip.GzipFile):
                f.write(str.encode('\n'.join(samplelist)))
            else:
                f.write('\n'.join(samplelist))



def getWriteBuff(file):
    suffix = os.path.splitext(file)[1]
    if suffix == '.gz':
        buff = gzip.GzipFile(file,'wb')
    else:
        buff = open(file,'w')
    return buff

if __name__ == '__main__':
    main()