import os
path = "E:\\新建文件夹\\Inuyasha_DVD_Complete_Simu\\[zmk.pw]犬夜叉\\"
files = os.listdir(path)
print(files)
for filename in files:
    id = filename[4:-4]
    # print(id)
    # id = filename.split()[1]

    new_name = 'Inuyasha.Ep'+id+'.x264.AC3_Simu.ass'
    os.rename(path+filename, path+new_name)
