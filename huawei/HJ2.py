# encoding=utf-8
"""
HJ2 计算某字母出现次数
"""

# input string 
input_str = input("")
input_char = input("").lower()

if input_str!="" and input_char!="":
    # Initial counter
    counter_char = 0

    # compare every char
    for counter_tmp in range(0, len(input_str)):
        if input_char == input_str[counter_tmp].lower():
            counter_char = counter_char + 1
        else:
            continue

    # print final counter
    print(counter_char)
