#encoding=utf-8
"""
HJ8 合并表记录
"""

result_dict = dict()

elem_num = eval(input())

for i in range(0, elem_num):
    input_tmp = input()
    key, value = input_tmp.split()
    key = eval(key)
    value = eval(value)
    if key not in result_dict.keys():
        result_dict[key] = value
    else:
        result_dict[key] = result_dict[key] + value

key_list = list(result_dict.keys())
key_list.sort()

for key in key_list:
    print("{:} {:}".format(key, result_dict[key]))
