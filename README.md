README
------

## 软件功能 ##

- **截取生物数据（fastq，fastq.gz）**
- **根据后缀名判断最终生成fq还是fq.gz**

**可以直接对gz文件进行处理，速度已经进行了优化**

---------------------------------------------

**OLD不再使用**

## 目前建议 一 ##

强烈建议使用解压后的fq文件进行处理，虽说目前程序可以使用fq.gz文件，但是对于速度的影响非常大

e.g.：
    fastq文件 ： test.fq.gz
    想要输出结果： result.fq.gz
    运行命令如下：
```shell
gunzip test.fq.gz && fastqSample -f test.fq -o result.fq -s xxxxx -seed xxxxx \
    && gzip test.fq && gzip result.fq
```

## 目前建议 二 ##

针对PE抽样，test.r1.fq.gz 和 test.r2.fq.gz，推介使用述方法：
```
gunzip test.r1.fq.gz && fastqSample -f test.r1.fq -o result.r1.fq -s xxxxx -seed 111 \
    && cp test.r1.fq.fqidx test.r2.fq.fqidx && gunzip test.r2.fq.gz && fastqSample -f test.r2.fq -o result.r2.fq -s xxxxx -seed 111 \
     &&gzip test.r1.fq && gzip result.r1.fq && gzip test.r2.fq && gzip result.r2.fq
```


-------------------------------------------

## 测试结果 ##

数据说明：

1. 测试的数据大小为2.6G（解压后）
2. 解压前数据大小513M
3. 测序长度为75
4. read条数为12,775,641

### fq.gz -> fq.gz(without index) ###

### fq.gz -> fq(without index) ###

### fq.gz -> fq.gz(without index,自解压) ###

### fq.gz -> fq.gz(index) ###

### fq.gz -> fq.gz(index,自解压) ###

### fq -> fq(without index) ###

### fq -> fq(index) ###


----------------------

### 20171012 ###

1. 通过subprocess改进了针对gz文件的处理，速度似乎能快不少

### 20170823 ###

1. 3.6G的fastq原始文件（测序长度为75），基于fastq建立索引13分中左右，包括从中随机取11条
2. 索引建立完毕后，在重复这项工作，从中随机取5条，0.3秒（最多测试过50000条，时间不到1秒）
3. 建立索引的确能够加快重复工作的速度

## 问题 ##

1. 并不是完全随机的，而是以100条read为一个整体，整体的随机，例如有10*100条read，取5条，则是从10里选5，然后各取一条read
2. 目前最后一个window是会被抛弃的，暂时没有想到很好的操作方式（待改进）
3. 在程序内部使用gzip感觉特别影响速度，但是具体的原因不知道处在哪块。