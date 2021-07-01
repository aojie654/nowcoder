# encoding=utf-8

"""
HJ13 句子逆序
"""

# Get input
input_str = input()
# Split with space and revese
input_list = input_str.split()
input_list.reverse()

# print every word in reversed list
for word_tmp in input_list:
    print(word_tmp, end=" ")
