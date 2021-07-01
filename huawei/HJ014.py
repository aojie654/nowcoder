# encoding=utf-8

"""
HJ14 字符串排序
"""

# Initial a list
result_list = list()
# Get the length of this list
list_len = int(input())

# Get input and append it to list for list_len times
for i in range(0, list_len):
    result_list.append(input())

# sort the list
result_list.sort()

# print every element in this list
for elem_tmp in result_list:
    print(elem_tmp)
