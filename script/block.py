#!/usr/bin/python3

import glob
rownum = 6
print("the rownum is %d" % rownum, flush=True)

for conf in range(0, 901, 10):
    print(conf, flush=True)
    filepath = "./pip_position/pip_position_b%04d*" % conf
    print(filepath, flush=True)
    files = glob.glob(filepath)
    print(len(files), flush=True)
    fp = open(files[0])
    ave = fp.read()
    fp.close()
    ave = list(map(float, ave.split()))
    ave = map(list, zip(*[iter(ave)]*rownum))
    avedata = sorted(ave, key=lambda k: [k[0], k[1], k[2], k[3]])
    for num in range(1, len(files)):
        print(num, flush=True)
        fp = open(files[num])
        tmp = fp.read()
        fp.close()
        tmp = list(map(float, tmp.split()))
        tmp = map(list, zip(*[iter(tmp)]*rownum))
        tmp = sorted(tmp, key=lambda k: [k[0], k[1], k[2], k[3]])
        for i in range(len(tmp)):
            for j in range(rownum):
                avedata[i][j] = avedata[i][j]+tmp[i][j]

    for i in range(len(avedata)):
        for j in range(rownum):
           # print(avedata[i][j])
            avedata[i][j] = avedata[i][j]/len(files)

    outputfile = "./download/pip_position_block_b%04d.txt" % conf
    with open(outputfile, 'w') as fp:
        for i in range(len(avedata)):
            for j in range(rownum-1):
                fp.write(str(avedata[i][j])+" ")
            fp.write("\n")


2 3 4 3 2 1
1 2 3 1 1 1
1 1 4 3 2 1
