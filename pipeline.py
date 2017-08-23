#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/8/16 下午2:05
# @Author  : chenyuelong
# @Mail    : yuelong_chen@yahoo.com
# @File    : pipeline.py
# @Software: PyCharm

import os, sys
import argparse
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))
from fastqTools import cutFastq,cutFastqC

def main():
    parser = argparse.ArgumentParser(description='截取数据，目前只能截取fastq')
    parser.add_argument('--fastq1','-f1',dest='fastq1',action='store',
                        help='支持两种格式，fastq或者gzip压缩的fastq（结尾为.gz）',
                        default='')
    parser.add_argument('--fastq2', '-f2', dest='fastq2', action='store',
                        help='支持两种格式，fastq或者gzip压缩的fastq（结尾为.gz）(可选)',
                        default='')
    parser.add_argument('--length','-l',dest='length',action='store',
                        help='read长度',default='')
    parser.add_argument('--size','-s',dest='size',action='store',
                        help='需要截取的数据量(默认单位为G)，如果需要截取1.2G数据则输入1.2',
                        default='1.2')
    parser.add_argument('--output','-o',dest='output',action='store',
                        help='截取输出前缀，默认压缩输出',default='')
    args = parser.parse_args()
    if args.fastq1 == '' or args.length == '' or args.size == '' or args.output =='':
        parser.print_help()
        exit(0)

    # cf = cutFastq.cutfastq(args.fastq,args.length,args.size,args.output)
    # cf.run()
    if args.fastq2 == '':
        cf = cutFastqC.cutfastqC(args.fastq1, length=args.length, size=args.size,outprefix= args.output)
    else:
        cf = cutFastqC.cutfastqC(args.fastq1,args.fastq2,length=args.length, size=args.size,outprefix= args.output)
    cf.run()



if __name__ == '__main__':
    main()