import sys
import os
import copy
import re

import numpy as np
import pandas as pd

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)


def check_match(match_str):
    if 'E' not in match_str:
        if re.search('[a-zA-Z]', match_str) is None:
            return True
        else:
            return False
    else:
        tmp_str = copy.deepcopy(match_str)
        re_search = re.search('[a-zA-Z]', tmp_str)
        while re_search is not None:
            re_search_group = re_search.group(0)
            if re_search_group != 'E':
                return False
            tmp_str = tmp_str[re_search.span()[1]:]
            re_search = re.search('[a-zA-Z]', tmp_str)
        return True


def return_all_row(data_str):
    data_str_list = []
    data_str = copy.deepcopy(data_str)
    re_search = re.search('\s\s(.*?)[0-9]\n', data_str)
    while re_search is not None:
        re_search_group = re_search.group(0)
        if check_match(re_search_group):
            data_str_list.append(re.findall(r'\d+\.?\d*E?[-+]?\d+', re_search_group))
        data_str = data_str[re_search.span()[1]:]
        re_search = re.search('\s\s(.*?)[0-9]\n', data_str)
    return data_str_list


if __name__ == '__main__':

    with open(project_path + '/data/data_saving_by_txt', 'r') as file:
        data_saving_by_txt = file.read()
    data = return_all_row(data_saving_by_txt)