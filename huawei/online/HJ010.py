#encoding=utf-8

"""
HJ10 字符个数统计
"""

input_str = input()
result_list = list()

for char_tmp in input_str:
    if ord(char_tmp) >= 0 and ord(char_tmp) <= 127:    
        if char_tmp in result_list:
            continue
        else:
            result_list.append(char_tmp)
    else:
        pass

print(len(result_list))
