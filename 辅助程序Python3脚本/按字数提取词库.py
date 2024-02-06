#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys;
import codecs;
import importlib,sys
importlib.reload(sys)
import re

# 此文件是 python3 脚本，读取第一个文件（网络收集的词库文件），每一行提取第一个元素（汉字单词），判断字数2~5及以上，分别放入不同的5个文件。
readfile = open(sys.argv[1]).readlines()
outfile_2 = open(sys.argv[1]+"-2.txt","w")
outfile_3 = open(sys.argv[1]+"-3.txt","w")
outfile_4 = open(sys.argv[1]+"-4.txt","w")
outfile_5 = open(sys.argv[1]+"-5.txt","w")
outfile_more = open(sys.argv[1]+"-more.txt","w")

for line in readfile:
    word = line.replace('\n','').split('\t')             # 去除回车号，以tab分割
    if re.search('(\d+)',word[0]):      # 是否包含数字
#        print(word[0])
        pass     # 跳过不操作
    elif re.search('[A-Za-z]',word[0]): # 是否包含字母
#        print(word[0])
        pass     # 跳过不操作
    else:
        word_length=len(word[0])              # 既不包含数字，也不包含字母，判断字数
#        print("word_length=",word_length)

        if word_length==2 :
            outfile_2.write(word[0]+'\n')     # 写入2字文件
        elif word_length==3 :
            outfile_3.write(word[0]+'\n')     # 写入3字文件
        elif word_length==4 :
            outfile_4.write(word[0]+'\n')     # 写入4字文件
        elif word_length==5 :
            outfile_5.write(word[0]+'\n')     # 写入5字文件
        else:
            outfile_more.write(word[0]+'\n')  # 更多字，写入more文件

