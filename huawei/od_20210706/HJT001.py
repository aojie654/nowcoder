# encoding = utf-8

"""
HJT001 列出数字的连续表示和.

1. 先输出数字等于自身
2. 逆序倒序开始递归相减
"""

# 获取输入的数字
num_input = int(input())
result_count = 0
# num_input = 14

def get_series(num_tmp):
    series = "-1"
    sum = 0
    num_tmpb = num_tmp
    while sum in range(0, num_input):
        sum = sum + num_tmp
        num_tmp = num_tmp - 1
    if sum == num_input:
        series = "{:}=".format(num_input)
        for i in range(num_tmp+1, num_tmpb, 1):
            series = "{:}{:}+".format(series, i)
        series = "{:}{:}".format(series, num_tmpb)
    else:
        pass

    return series


if __name__ == '__main__':
    if num_input in range(1, 1001):
        # 初始化一个临时计数变量
        num_inc = num_input
        while (num_inc >=1):
            series = get_series(num_tmp=num_inc)
            if series != "-1":
                print(series)
                result_count = result_count + 1
            num_inc = num_inc - 1
        print("Result:{:}".format(result_count))