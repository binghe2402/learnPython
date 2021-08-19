#!/usr/bin/python3

import glob
rownum = 7
print("the rownum is %d" % rownum, flush=True)

for conf in range(0, 901, 10):
    print(conf, flush=True)
    filepath = "/vol7/home/fengxu/sxia/conf24/field_selection_twop/data/pip_random/pip_random_b%04d*" % conf
    print(filepath, flush=True)
    files = glob.glob(filepath)
    print(len(files), flush=True)
    fp = open(files[0])
    ave = fp.read()
    fp.close()
    ave = list(map(float, ave.split()))
    ave = map(list, zip(*[iter(ave)]*rownum))
    avedata = list(ave)
    for num in range(1, len(files)):
        print(num, flush=True)
        fp = open(files[num])
        tmp = fp.read()
        fp.close()
        tmp = list(map(float, tmp.split()))
        tmp = map(list, zip(*[iter(tmp)]*rownum))
        tmp = list(tmp)
        for i in range(len(tmp)):
            for j in range(rownum):
                avedata[i][j] = avedata[i][j]+tmp[i][j]

    for i in range(len(avedata)):
        for j in range(rownum):
           # print(avedata[i][j])
            avedata[i][j] = avedata[i][j]/len(files)

    outputfile = "./pip_random/pip_random_block_b%04d.txt" % conf
    with open(outputfile, 'w') as fp:
        for i in range(len(avedata)):
            for j in range(rownum-1):
                fp.write(str(avedata[i][j])+" ")
            fp.write("\n")
