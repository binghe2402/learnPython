#!/usr/bin/python3

import glob
import os

rownum = 7
print("the rownum is %d" % rownum, flush=True)
directory = ["stout0", "stout5", "stout10", "stout15"]


for dire in directory:
    if not os.path.exists("./block_mom002/%s" % (dire)):
        os.mkdir("./block_mom002/%s" % (dire))
        print("establish directory %s" % dire)
    for conf in range(0, 491, 10):
        print(conf, flush=True)
        filepath = "./mom002/%s/phi_wall_source_a%04d*" % (dire, conf)
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

        outputfile = "./block_mom002/%s/phi_wall_source_block_a%04d.txt" % (dire, conf)
        with open(outputfile, 'w') as fp:
            for i in range(len(avedata)):
                for j in range(rownum):
                    fp.write(str(avedata[i][j])+" ")
                fp.write("\n")
