# encoding=utf-8

"""
HJT003 最长子串
in: 
abC124ACb

out:
4
"""

# Get input
input_str = input()
# input_str = "abC124ACb"
# input_str = "asdfghjkl"
# input_str = "1234567890"
# input_str = "axd3413df1234567890a1"
# input_str = "axd3413df1234567890a123456anz"
len_input_str = len(input_str)
max_length = -1
max_length_cur = -1

stats_list = [0, 0]
stats_list_b = [0, 0]
str_cur = ""

for pos_i in range(0, len_input_str):
    for pos_j in range(pos_i, len_input_str):
        if (("A" <= input_str[pos_j] <= "Z") or ("a" <= input_str[pos_j] <= "z")):
            stats_list[0] = stats_list[0] + 1
        elif ("0" <= input_str[pos_j] <= "9"):
            stats_list[1] = stats_list[1] + 1
        if stats_list[0] > 1:
            max_length_cur = -1
            stats_list = [0, 0]
            break
        else:
            max_length_cur = stats_list[0] + stats_list[1]
        if ((max_length < max_length_cur) and (max_length_cur >= 2)):
            max_length = max_length_cur
            stats_list_b = stats_list
    stats_list = [0, 0]
    max_length_cur = -1
    if ((len_input_str - pos_i) < max_length):
        print(pos_i, input_str[pos_i])
        break
if stats_list_b[0] == 0:
    max_length  = -1
print(max_length)
