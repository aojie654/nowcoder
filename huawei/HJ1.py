# encoding=utf-8

"""
HJ1 字符串最后一个单词的长度
"""

# input string 
input_str = input("")

if input_str != "":
    # split to list
    input_list = input_str.split(" ")

    # get last element
    word_last = input_list[-1]

    # get length
    word_last_len = len(word_last)

    # print length
    print(word_last_len)
