#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys;
import codecs;
import requests
import re

# 此文件是 python3 脚本，读取已下载的四级行政区划 html 网页（目录和文件），提取所需的字段，放入新的输出文件。

outfile = open("./test_name.txt",'w')                   # 先创建一个空的文本
word="</td></tr><tr class"                              # 网页中包含的特定格式
pat = re.compile('<[^>]+>', re.S)                       # 去除HTML中标签
def get_filelist(dir):                                  # 获取文件清单
    for home, dirs, files in os.walk(dir):              # 遍历文件和目录
        dirs.sort()                                     # 排序文件
        files.sort()                                    # 排序目录
        for filename in files:
            fullname = os.path.join(home, filename)     # 完整的文件名和目录
            readfile = open(fullname, encoding="unicode_escape").readlines()   # 打开文件
            for line in readfile:                       # 每一行
                search_word = re.search(word, line)     # 查找网页中包含的特定格式
                if search_word:                         # 如果包含有
                    data = line.encode("latin1") .decode("gb18030") 
# 将原网页GB2312转码成latin1编码（使用encode函数） ，再解码成utf8编码（使用decode函数）
                    line_list = data.split('</tr>')     # 以网页表格中的每行分割
                    for each_line in line_list:         # 表格中的每一行
                        word_list = each_line.split('</td>')    # 以网页表格中的每个单元格分割
#                        print (len(word_list))                 # 单元格个数
                        if len(word_list)==3:                   # 收集到四级地名为止，
                            if "市辖区" in word_list[1]: # 剔除不需要的数据
                                pass                    # 跳过不操作
                            else:
                                word_need = pat.sub('', word_list[0])+'\t'+pat.sub('', word_list[1]+'\n')          # 去除HTML中标签，组合，以Tab键分隔
#                               print (word_list)           # 显示提取了哪些词汇
                                outfile.write(word_need)    # 写入输出文件
#                        elif len(word_list)==4:            # 如果需要四级以上的地名，即“居委会”
#                            pass                           # 跳过不操作，收集到四级地名为止，街道居委会每个城市每年都在增加，更新量太大
#                            word_need = pat.sub('', word_list[0])+'\t'+pat.sub('', word_list[2]+'\n') # 去除HTML中标签，组合，以Tab键分隔
#                            outfile.write(word_need+'\n')       # 写入输出文件
#                            print (word_need)                   # 显示提取了哪些词汇
#                            outfile.write(word_need)       # 写入输出文件
if __name__ == "__main__":
    get_filelist('./2020/65')                               # 在此指定程序搜索的起始目录
