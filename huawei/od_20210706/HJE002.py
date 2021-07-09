# encoding=utf-8

"""
HJE002 求方阵总和
"""

# 初始化总和
sum_result = 0

# 获取边长
length_sq = int(input())

# 重复 length_sq * length_sq 次
for count_row in range(length_sq):
    input_list = input().split()
    for number_line in input_list:
        sum_result = sum_result + int(number_line)

# 输出总和
print(sum_result)
