#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import os
import sys;
import codecs;
import importlib,sys
importlib.reload(sys)

#此文件是 python3 脚本，用于排除原词库已有的字词，或者黑名单。用python字典的方式，速度特快，适合百万千万以上级别的词库比较。
#从第二个文件里的提取词组，与第一个文件的提取的关键字（字典）比较，如果不重复，则写入C文件。
#注意所有文件都应保存成utf-8的文本文件，末尾不要有空行。
 
fa=open(sys.argv[1]).readlines()                # 黑名单
fb=open(sys.argv[2]).readlines()                # 待清理的文件
outfile = open(sys.argv[2]+"-已清理.txt","w")   # 输出已清理的文件

Hei={}                                          # 黑名单专用字典

for x in fa:
    temp_fa = x.replace('\n','').split('\t')    # 去除回车号，以制表符分割
    word_fa = temp_fa[0].encode("gb18030")      # 按 gb18030 编码，再放入字典，否则查询不出
    Hei[word_fa] = temp_fa[0]
#print (Hei)                                     # 测试显示字典结果


for i in fb:
#    print i
    temp_fb = i.replace('\n','').split('\t')    # 去除回车号，以制表符分割
    word_fb = temp_fb[0].encode("gb18030")      # 按 gb18030 编码，否则无法比较
    if word_fb not in Hei:
        w = i                                   # 这里可以调整格式
        outfile.write(''.join(w))               # 写入C文件
    else:
        print (temp_fb[0])                      # 显示清理了哪些词汇
#fc.close()
