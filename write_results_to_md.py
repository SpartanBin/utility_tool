"""
    转换结果表格到markdown格式
"""


import os
from itertools import product

import numpy as np
import pandas as pd


def write_pdDataFrame_to_mkdown(pd_DataFrame, save_path, save_file_name):
    '''
    把pd.DataFrame写为mkdown表格，会保存在项目的根目录，注意列名不能有中文
    :param pd_DataFrame: pd.DataFrame
    :param save_path: 保存文件路径，str
    :param save_file_name: 保存文件名，str
    :return: None
    '''

    # mkdown表格格式如下
    # HEAD = '''
    # |       Forecast Dataset        |  Average  |   2970    |
    # | :---------------------------: | :-------: | :-------: |
    # | ```kill``` | 2 | 2 |
    # '''

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    col_name_list = list(pd_DataFrame.columns.values)

    head = '\n|'
    spacing_length_list = []

    add_title = '       |'
    head += add_title
    spacing_length_list.append(len(add_title))

    for col_name in col_name_list:
        add_title = '  ' + col_name + '  |'
        head += add_title
        spacing_length_list.append(len(add_title))
    head += '\n|'
    for spacing_length in spacing_length_list:
        head += ' :' + '-' * (spacing_length - 5) + ': |'

    value_text = ''
    np_array = pd_DataFrame.values
    pd_index = pd_DataFrame.index
    for i, row in enumerate(np_array):
        value_text += '\n| {} |'.format(pd_index[i])
        for value in row:
            value_text += ' {} |'.format(value)

    index = save_file_name.find('.')
    if index > 0:
        save_file_name = save_file_name[: index]
    with open(save_path + '/{}.md'.format(save_file_name), 'w') as file:
        file.write(head + value_text)