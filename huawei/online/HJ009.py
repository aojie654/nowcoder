#encoding=utf-8
"""
HJ9 提取不重复的整数
"""

result_str = str()
input_str = str(input())

if input_str[-1]!="0":
    for char_tmp in input_str[::-1]:
        if char_tmp in result_str:
            continue
        else:
            result_str = result_str + char_tmp

    print(result_str)
else:
    pass