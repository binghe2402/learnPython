import os
import re

delta_t = 10

path_data = ''
path_filter = './test'

file_filter = os.walk(path_filter)

with open('e://project_data//file_selector//random_list_b0000.txt', 'r') as random_list:
    select_lst = random_list.readlines()


for roots, dirs, files in file_filter:
    # print(root_path)
    # print(file_name)
    for file_name in files:
        file_name = file_name.replace('random_pp', 'position')

        with open(path_data + file_name, 'r') as data:
