# encoding=utf-8

"""
HJ15 求int型正整数在内存中存储时1的个数
"""

# Get input, transfer it to bin char and initial counter
input_str = int(input())
result_str = bin(input_str)[2:]
counter_t = 0

# Count the char "1"
for char_t in result_str:
    if char_t == "1":
        counter_t = counter_t + 1
    else:
        continue

# Print counter "1"
print(counter_t)
