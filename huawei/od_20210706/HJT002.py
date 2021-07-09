# encoding=utf-8

"""
HJT002 非严格递增数字序列
"""

# Get input
input_str = input()
# input_str = "abc2234019A334bc"
max_length = 1
max_length_cur = 1

char_cur = ""
char_last = ""
for char_cur in input_str:
    if "0" <= char_cur <= "9":
        if (char_last != ""):
            if (char_cur >= char_last):
                max_length_cur = max_length_cur + 1
            else:
                max_length_cur = 1
        char_last = char_cur
    else:
        char_last = ""
        max_length_cur = 1
    if (max_length < max_length_cur):
        max_length = max_length_cur

print(max_length)
