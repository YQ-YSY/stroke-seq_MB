#!/usr/bin/python3
#-*- coding: UTF-8 -*-
import sys;  

# 此文件是 python3 脚本，删除第一个文件中的重复行，并生成已去重文件
readfile = open(sys.argv[1]).readlines()
outfile = open(sys.argv[1]+"-已去重.txt","w")

lines_seen = set()   # 函数 set() 创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。

for line in readfile:
    if line not in lines_seen:   # 判断是否在库中
        outfile.write(line)
        lines_seen.add(line)     # 累加入库
outfile.close()

