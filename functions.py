import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def readfile(file_path):
    with open(file_path) as f:
        while True:
            try:
                line = next(f)
            except StopIteration:
                break
            split_str = line.split('\n')
            yield split_str


file_name = 'apache_logs.txt'
path = f'{DATA_DIR}\\{file_name}'


# if os.path.exists(path):
#     #f = find(path, "83.149.9.216")





# sorted(split_str_arr, key=lambda v: v, reverse=True))
# searchpattern = re.compile('.*{}.*'.format(word))
# sqls1 = list(filter(lambda x: searchpattern.search(x) and x, split_str))
# print(sqls1)

# split_str_arr = list(map(lambda x: x.split(' ')[0], split_str))
# print(list(filter(lambda x: x != '', split_str_arr)))

# print(list(set(list(filter(lambda x: x != '', split_str_arr)))))

file_name = 'apache_logs.txt'
path_ = f'{DATA_DIR}\\{file_name}'

# def my_decorator(a_function_to_decorate):
#     def wrapper(**kwargs):
#         def readfile(path):
#             with open(path, 'r') as f:
#                 all_str = f.read()
#                 split_str = all_str.split('\n')
#                 return split_str
#         return a_function_to_decorate(readfile(path_), **kwargs)
#     return wrapper
#
#
# @my_decorator
# def map_file(split_str: list, row: int, flag=False):
#     split_str = list(filter(lambda x: x != '', split_str))
#     split_str_arr = list(map(lambda x: x.split(' ')[row], split_str))
#     if flag:
#         return list(set(split_str_arr))
#     else:
#         return split_str_arr
#
#
# @my_decorator
# def filter_file(split_str: list, word):
#     searchpattern = re.compile('.*{}.*'.format(word))
#     filter_data = list(filter(lambda x: searchpattern.search(x) and x, split_str))
#     return filter_data
#
# @my_decorator
# def sort_file(split_str: list, reverse=False, limit=None):
#     sorted_data = sorted(split_str, key=lambda v: v, reverse=reverse)
#     return sorted_data[:limit]


def map_file(split_str, flag=False, row=0):
    split_str = list(filter(lambda x: x[0] != '', list(split_str)))
    split_str_arr = list(map(lambda x: re.split(r'[\s-]+(?!\+\d+)', x[0])[row], split_str))
    if flag:
        return list(set(split_str_arr))
    else:
        return split_str_arr

def my_decorator(a_function_to_decorate):
    def wrapper(**kwargs):
        splt_str = map_file(readfile(path))
        return a_function_to_decorate(splt_str, **kwargs)
    return wrapper

@my_decorator
def sort_file(split_str: list, reverse=False, limit=None):
    sorted_data = sorted(split_str, key=lambda v: v, reverse=reverse)
    return sorted_data[:limit]

for item in sort_file():
    print(item)