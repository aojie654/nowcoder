# encoding = utf-8

"""
HJE001 求两数之和
"""

# 获取输入
input_str = input()

# 以空格分割获取值 a b
a, b = input_str.split()
# 转换为整数
a, b = int(a), int(b)

# 求和
sum_ab = a+b

# 输出
print(sum_ab)