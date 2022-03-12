from typing import Generator, Union, List
import re


def readfile(file_path: str) -> Generator:
    with open(file_path) as f:
        while True:
            try:
                line = next(f)
            except StopIteration:
                break
            split_str = line.split('\n')
            yield split_str

#Идея с декоратором не реализована.
# def file_decorator(a_function_to_decorate):
#     def wrapper(**kwargs):
#         split_str = readfile(kwargs['path'])
#         return a_function_to_decorate(split_str, **kwargs)
#     return wrapper


def map_file(split_str: Union[List, Generator], row: int = 0) -> List:
    split_ = list(filter(lambda x: x[0] != '', split_str))
    if isinstance(split_str, list):
        split_str_arr = list(map(lambda x: re.split(r'[\s-]+(?!\+\d+)', x)[row], split_))
    else:
        split_str_arr = list(map(lambda x: re.split(r'[\s-]+(?!\+\d+)', x[0])[row], list(split_)))
    return split_str_arr


def sort_file(split_str: Union[List, Generator], reverse: str = 'asc') -> List:
    if reverse == 'desc':
        flag = True
    else:
        flag = False
    if not isinstance(split_str, list):
        split_str = list(map(lambda x: x[0], list(split_str)))
    sorted_data = sorted(split_str, key=lambda v: v, reverse=flag)
    return sorted_data


def unique_(split_str: Union[List, Generator]) -> List:
    if not isinstance(split_str, list):
        split_str = list(map(lambda x: x[0], list(split_str)))
    return list(set(split_str))


def regex_search(split_str: Union[List, Generator], search_pattern: str) -> List:
    if not isinstance(split_str, list):
        filter_data = filter(lambda x: re.compile(search_pattern).search(x[0]), list(split_str))
        split_str_arr = list(map(lambda x: x[0], list(filter_data)))
    else:
        filter_data = filter(lambda x: re.compile(search_pattern).search(x), split_str)
        split_str_arr = list(map(lambda x: x, list(filter_data)))
    return split_str_arr


def limit_data(split_str: Union[List, Generator], limit: int = None) -> List:
    if not isinstance(split_str, list):
        split_str = list(map(lambda x: x[0], list(split_str)))
    return split_str[:limit]
