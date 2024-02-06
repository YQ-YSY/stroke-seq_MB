#!/usr/bin/python3
#-*- coding: UTF-8 -*-
import sys;  

# 此文件是 python3 脚本，读取第一个文件中单词，按 gb18030 排序（便于人工浏览），生成排序后的文件
readfile = open(sys.argv[1]).readlines()
outfile = open(sys.argv[1]+"-已排序.txt","w")

PP={}                                     # 排序专用字典

for x in readfile:
    xx = x.replace('\n','').split('\t')   # 去除回车号，以制表符分割
#    print xx[1],xx[5],xx[7]              # 测试显示（如果有多列）
    str = xx[0].encode("gb18030")         # 按 gb18030 编码，再放入字典
    PP[str]=xx[0]
#print (PP)                         # 测试显示字典结果

z=zip(PP.values(),PP.keys())       # 利用zip函数把dict转换成一个列表，
dd=sorted(z)                       # 对这个列表进行sorted排序
#print (dd)                         # 测试显示列表结果

for i in dd:
    outfile.write(''.join(i[0]+'\n'))               # 写入输出文件（检查输出文件的头几行，也容易发现错误词组）
outfile.close()

