'''
数据处理

功能说明
    从path_fileter路径获取文件列表，作为过滤规则，
    筛选path_data下的数据文件。

    读取每一个数据文件，提取文件名中的 _t0_x0_y0_z0 坐标，
    筛选对应组态的 random_list 文件中 t 坐标为 t0 + delta_t 的行，t x y z。
    二者相减得到相对坐标，  t-t0 = delta_t, x-x0, y-y0, z-z0
    所有坐标值 t∈[0,48). x,y,z∈[0,24)
    取出数据文件中，坐标值为相对坐标的行，
    按照 random_list 的顺序重新储存。

文件说明
    数据文件
        每行为6个数字，以空格间隔。
        前4个为 int，表示坐标值 t,x,y,z，
        后两个为 6位精度的 float 的科学计数法,%e格式(即'%.6fe[+-]%02d')，表示复数的实部和虚部，

        类型      int  int  int  int   float,e     float,e
        含义       t    x    y    z      re           im
        样例       0    1    2    0  1.000000-02  1.000000+02


    random_list文件
        每行4个数字，以空格间隔。
        4个均为 int，表示坐标值 t,x,y,z，

        类型      int  int  int  int
        含义       t    x    y    z
        样例       0    1    2    0
'''

import os
# import re
# import numpy as np

delta_t = 10
range_t = 48
range_xyz = 24

path_data = r''
path_filter = r'./test'
path_list = r'e:/project_data/file_selector/'
out_path = r''
out_file_name_pre = 'pip_position_u_block_'
file_ext = '.txt'
# coordinate
coord_pos = [19, 22, 25, 28]
coord_len = 2
# configuration
conf_pos = 13
conf_len = 5

file_filter = sorted(os.listdir(path_filter))


def get_random_list(path_list, conf, pre='random_list_'):
    # 储存所有random_list的数据，
    # 结构为以 t 为索引的 t 个list，
    # 每个list中为这个t对应的所有(x,y,z)元组
    file_name = pre+conf+'.txt'
    with open(os.path.join(path_list, file_name), 'r') as random_list:
        select_lst = [[] for i in range(range_t)]
        for line in random_list.readlines():
            t, x, y, z = map(int, line.split())
            select_lst[t].append((x, y, z))
    return select_lst


def main():
    # print(len(file_filter))
    for file_name in file_filter:
        file_name = file_name.replace('random_pp', 'position')
        print(file_name)

        # 提取组态
        conf = file_name[conf_pos:conf_pos+conf_len]

        select_lst = get_random_list(path_list, conf)

        # 提取文件名的坐标值
        # manual
        t, x, y, z = (int(file_name[i:i+coord_len]) for i in coord_pos)
        # auto
        # t, x, y, z = [int(i) for i in re.findall(r'(?<=_)\d{2}', file_name)]

        # 计算相对坐标
        # def rela(arg_l, arg): return (arg_l-arg) % range_xyz
        select_lst_rela = [((x_l-x) % range_xyz,
                            (y_l-y) % range_xyz,
                            (z_l-z) % range_xyz)
                           for x_l, y_l, z_l in select_lst[(t+delta_t) % range_t]]
        # print(len(select_lst_rela))

        data = {}
        # 读取数据文件
        with open(os.path.join(path_data, file_name), 'r') as data_file:
            # data_line = True
            # while data_line:
            #     data_line = data_file.readline()
            for data_line in data_file.readlines():
                number_list = data_line.split()
                # 提取相对坐标 t 匹配的行
                if int(number_list[0]) == delta_t:
                    # 以相对坐标 t,x,y,z 为key，储存该数据行字符串
                    pos = tuple(int(i) for i in number_list[1:4])
                    # if pos in data:      # 查重
                    #     print(pos)
                    data[pos] = data_line

        # 按照顺序追加写入到输出文件
        with open(os.path.join(out_path, out_file_name_pre+conf+file_ext), 'a') as out:
            for pos in select_lst_rela:
                out.write(data[pos])


if __name__ == "__main__":
    main()
