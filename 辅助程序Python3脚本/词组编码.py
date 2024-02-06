#!/usr/bin/python3
#-*- coding: UTF-8 -*-

import os
import sys;
import codecs;
import importlib,sys
importlib.reload(sys)

# 此文件是 python3 脚本，将第三个文件里的词组中分割汉字，
# 按第一个文件的六全码和第二个文件的精简码，对第三个文件的词组进行编码，写入输出文件。
# 由于不是每个汉字都有精简码，因此二个词组编码一个是纯六全码，另一个是精简码与六全码的混合编码。
# 注意所有文件都应保存成utf-8的文本文件，末尾不要有空行。
 
fa=open(sys.argv[1]).readlines()           # 第一个文件六全码
fb=open(sys.argv[2]).readlines()           # 第二个文件精简码
fc=open(sys.argv[3]).readlines()           # 第三个文件无编码词组
fd=open(sys.argv[3]+"-已编码.txt",'w')

LQM={}   # 六全码专用字典
JJM={}   # 精简码专用字典

for x in fa:
    xx = x.replace('\n','').split('\t')    # 去除回车号，以制表符分割
    LQM[xx[0]] = xx[1]                     # 放入六全码字典
#print (LQM)                                # 测试显示字典结果

for y in fb:
    yy = y.replace('\n','').split('\t')    # 去除回车号，以制表符分割
    JJM[yy[0]] = yy[1]                     # 放入精简码字典
#print (JJM)                                # 测试显示字典结果

for z in fc:
    zz = z.replace('\n','')                # 去除回车号
#    print (zz)                             # 测试显示一行一个词组
    add_JJM = ""                           # 用于精简码的词组合并编码
    add_LQM = ""                           # 用于六全码的词组合并编码
    NN = 0                                 # 用于标记是否有非汉字的特殊字符
    for i in zz :
#        print (i)                          # 测试显示拆分汉字的结果
        JJM_i = JJM.get(i)                 # 获取该汉字的精简码
        LQM_i = LQM.get(i)                 # 获取该汉字的六全码

        if JJM_i == None :                 # 如果该汉字无精简码，即为None
            JJM_i = LQM_i                  # 则让精简码等同于六全码。
        if LQM_i == None :                 # 如果该汉字无六全码，即为None
#            print (i,LQM_i)
            NN = 1                         # 标记有非汉字的特殊字符，无编码
        else:
            add_JJM = add_JJM+"."+str(JJM_i)  # 逐个串联合并该词组的精简码
            add_LQM = add_LQM+"."+str(LQM_i)  # 逐个串联合并该词组的六全码
    add_JJM = add_JJM[1:]                  # 最后去除多余的第一个点号
    add_LQM = add_LQM[1:]                  # 最后去除多余的第一个点号

    if NN == 0:                            # 一切正常，无非汉字的特殊字符，可以写入文件
#        print (add_JJM,"---",add_LQM)      # 测试显示该词组编码的结果
        if add_JJM == add_LQM :            # 如果该词组的精简码和六全码完全相同
            w = zz+'\t'+add_LQM+'\n'       # 只写入六全码一个编码即可，非核心词库不需要加词频
#            w = zz+'\t'+add_LQM+'\t'+"800"+'\n' # 核心词库词频设为800
        else:                              # 如果该词组的精简码和六全码不同
            w = zz+'\t'+add_JJM+'\n'+zz+'\t'+add_LQM+'\n'    # 写入精简码和六全码，非核心词库不需要加词频
#            w = zz+'\t'+add_JJM+'\t'+"800"+'\n'+zz+'\t'+add_LQM+'\t'+"800"+'\n'    # 核心词库词频设为800
        fd.write(w)                        # 正式写入d文件
    else:
        pass                               # 带有非汉字的特殊字符，无编码，跳过不写入文件
#fd.close()
