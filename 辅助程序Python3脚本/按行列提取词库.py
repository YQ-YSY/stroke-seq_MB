#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys;
import codecs;
import importlib,sys
importlib.reload(sys)
import re

# 此文件是 python3 脚本，读取第一个文件（网络收集的词库文件），每一行提取第N个元素（汉字单词，不同的输入法词库码表所在位置有可能不同），判断没有英文或数字，且不属于第二个文件“错别字恶俗词汇黑名单”，则放入新的输出文件。
readfile = open(sys.argv[1]).readlines()
blacklist = open(sys.argv[2]).readlines()                # 黑名单
outfile = open(sys.argv[1]+"-已提取.txt","w")

Hei={}                                                   # 黑名单专用字典
for x in blacklist:
    temp_blacklist = x.replace('\n','').split('\t')      # 去除回车号，以制表符分割
    word_blacklist = temp_blacklist[0].encode("gb18030") # 按 gb18030 编码，再放入字典，否则查询不出
    Hei[word_blacklist] = temp_blacklist[0]
#print (Hei)                                             # 测试显示字典结果

for line in readfile:
    word = line.replace('\n','').split('\t')    # 去除回车号，以tab分割
    word_need = word[0]                         # 不同的输入法词库码表所在位置有可能不同，可能是第一个，也可能是第二第三个
    word_readfile = word_need.encode("gb18030") # 按 gb18030 编码，否则无法与黑名单专用字典比较

    if re.search('(\d+)',word_need):            # 是否包含数字
#        print(word_need)                       # 显示清理了哪些词汇
        pass     # 跳过不操作
    elif re.search('[A-Za-z]',word_need):       # 是否包含字母
#        print(word_need)                       # 显示清理了哪些词汇
        pass     # 跳过不操作
    elif word_readfile in Hei:
#        print (word_need)                       # 显示清理了哪些词汇
        pass     # 跳过不操作
    else:
        outfile.write(word_need+'\n')           # 写入输出文件

