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
i=1



N=10
#设定任务数量
                                                
core_part=["th_mt1","th_ft1"]
#分区列表


part_x={"th_mt1":"cn385,cn456,cn470",\
        "th_ft1":""}
#分区禁用的节点

#part_x=dict(zip(core_part,part_x))




confid={"th_mt1":['%04d'%id for id in [0]+range(10,21,2),\
        "th_ft1":['%04d'%id for id in range(520,550+1,10)]}
        confid[x][nn[x]]
        
#分区提交任务的编号



nn={"th_mt1":0,\
    "th_ft1":0}
#分区已提交的任务



while core_part:
#当分区列表不为空
   
    os.system('yhq>yhq.txt')
    time.sleep(1)

    
    f = open("yhq.txt")
    lines = f.readlines()
    f.close()
    
    lines = [line.rstrip('\n').split() for line in lines]
    item=lines[0]
    lines=lines[1:]
        
    part = [x[1] for x in lines]
#   统计当前任务分区        

    for x in core_part:              #在分区列表中遍历每个分区
        if part.count(x)<N:          #在当前任务分区中统计分区x的个数，即为当前正在分区x执行的任务数。如小于设定的任务数N，则进行提交
        
            os.system('yhbatch -n 512 -x '+part_x[x]+' -p '+x+' ./contraction'+confid[x][nn[x]]+'/run'+confid[x][nn[x]]+'.sh')
 #                                    -x  +part_x[x]  设置禁用节点     -p '+x   设置运行分区
 #                                    ./contraction'+confid[x][nn[x]]+'/run'+confid[x][nn[x]]+'.sh'    提交路径，路径中confid[x][nn[x]]为文件编号，是字典数组confid{分区:[序列号]}的元素
 #                                    nn[x]为字典，是{分区:已提交任务数}

            print 'yhbatch -n 512 -x '+part_x[x]+' -p '+x+' ./contraction'+confid[x][nn[x]]+'/run'+confid[x][nn[x]]+'.sh'
            nn[x]=nn[x]+1
            print "当前时间戳为:", time.time()
            
            print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n'
            
            if nn[x]>=len(confid[x]):
                core_part.remove(x)
#           当分区已提交的任务数量 > 分区任务的编号的数目，则该分区的任务已全部提交，移除该分区     
       
# =============================================================================
#     for line in lines:
#         if time.strptime(line[TIME],"%M:%S")>time_out:
#             print line[TIME]
# =============================================================================

    time.sleep(5)
    print "i=",i
    print "------------------------------------------------------------"
    i=i+1
