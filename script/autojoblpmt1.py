#!/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 23:54:42 2019

@author: binghe2402

autoyhbatch on Tianhe 

version 0.1beta

"""

import time
import os
i = 1


N = 11
# 设定任务数量

core_part = ["th_mt1"]
# 分区列表


part_x = {"th_mt1": "cn1669,cn167[4-6,8],cn168[1-2],cn1693,cn1703,cn1717,cn1722,cn173[1,3],cn174[2,5-6,9],cn1750,cn1805,cn182[2,4,6],cn186[2,5],cn1909,cn191[2,5],cn1921,cn1939,cn194[2,6],cn201[5,8],cn2027,cn2034,cn204[1-2,6],cn2058,cn206[0,2,4,6],cn207[0,2,6-8],cn208[1,5-6],cn2095,cn210[5,7-8],cn211[6,8],cn2126,cn2130,cn215[2,5],cn223[6,8],cn224[0,9],cn2253,cn2269,cn228[0,8],cn229[1-2,8],cn230[3,4,9],cn231[1,3,7],cn232[0-2,5-8],cn233[3,6-8],cn234[6,8,9],cn236[0-1,5,7,9],cn237[2-4,9],cn238[6,8],cn239[2-4],cn240[4,5],cn241[2,4],cn242[0,4,6],cn243[0,7],cn244[0,2,8],cn246[1-3,5,8],cn247[2,4-5,7],cn2482,cn251[4,6],cn2522,cn253[0,4,8],cn254[6,9],cn255[1,3,5],cn256[2,6,8-9],cn257[0,2-3,6,8],cn2580,cn259[1,4-8],cn260[4,9],cn261[2-4],cn2685,cn2742,cn280[4,9],cn2814,cn2890,cn2901,cn2953,cn297[3,5],cn299[6,8],cn303[2,5],cn322[2,9],cn3236,cn3262,cn327[7-9],cn3389,cn3441,cn3467,cn3474,cn3508,cn3550,cn3649,cn369[1-4,6],cn3763,cn385[1,8],cn3947,cn3965"}
# 分区禁用的节点

# part_x=dict(zip(core_part,part_x))

confid = {"th_mt1": ['%02d' % id1+'%04d' % id2 for id2 in range(
    0, 600+1, 10)+range(6, 596+1, 10) for id1 in range(1, 16)]}
# 分区提交任务的编号

nn = {"th_mt1": 0}
# 分区已提交的任务


while core_part:
    # 当分区列表不为空

    os.system('yhq>yhq.txt')
    time.sleep(1)

    f = open("yhq.txt")
    lines = f.readlines()
    f.close()

    lines = [line.rstrip('\n').split() for line in lines]
    item = lines[0]
    lines = lines[1:]

    part = [x[1] for x in lines]
#   统计当前任务分区

    for x in core_part:  # 在分区列表中遍历每个分区
        if part.count(x) < N:  # 在当前任务分区中统计分区x的个数，即为当前正在分区x执行的任务数。如小于设定的任务数N，则进行提交

            os.system('yhbatch -n 512 -t 50 -x ' +
                      part_x[x]+' -p '+x+' ./contraction'+confid[x][nn[x]][2:]+'/run'+confid[x][nn[x]]+'.sh')
 #                                    -x  +part_x[x]  设置禁用节点     -p '+x   设置运行分区
 #                                    ./contraction'+confid[x][nn[x]]+'/run'+confid[x][nn[x]]+'.sh'    提交路径，路径中confid[x][nn[x]]为文件编号，是字典数组confid{分区:[序列号]}的元素
 #                                    nn[x]为字典，是{分区:已提交任务数}

            print 'yhbatch -n 512 -t 50 -x '+part_x[x]+' -p '+x+' ./contraction'+confid[x][nn[x]][2:]+'/run'+confid[x][nn[x]]+'.sh'
            nn[x] = nn[x]+1
            print "当前时间戳为:", time.time()

            print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n'

            if nn[x] >= len(confid[x]):
                core_part.remove(x)
#           当分区已提交的任务数量 > 分区任务的编号的数目，则该分区的任务已全部提交，移除该分区

# =============================================================================
#     for line in lines:
#         if time.strptime(line[TIME],"%M:%S")>time_out:
#             print line[TIME]
# =============================================================================

    time.sleep(5)
    print "i=", i
    print "------------------------------------------------------------"
    i = i+1
