# encoding=utf-8

"""
HJ15 求int型正整数在内存中存储时1的个数
"""

# 获取输入, 转换为二进制, 并初始化计数器
input_str = int(input())
result_str = bin(input_str)[2:]
counter_t = 0

# 计算1的数量
for char_t in result_str:
    if char_t == "1":
        counter_t = counter_t + 1
    else:
        continue

# 将1的数量输出
print(counter_t)
