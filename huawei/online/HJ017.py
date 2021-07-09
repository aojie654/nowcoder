# encoding = utf-8

"""
HJ17 坐标移动
"""


# 获取输入
input_str = input()

# 以";"分割
input_list = input_str.split(";")
# 初始化坐标
position_tmp = [0, 0]
# 遍历每一个元素
for elem_tmp in input_list:
    # 跳过不合法的元素
    try:
        # 获取方向和步长
        face_to = elem_tmp[0].lower()
        length_step = eval(elem_tmp[1:])
        # 根据 "A","D" 判断左右
        if face_to == "a":
            position_tmp[0] = position_tmp[0] - length_step
        elif face_to == "d":
            position_tmp[0] = position_tmp[0] + length_step
        # 根据 "W","S" 判断上下
        elif face_to == "w":
            position_tmp[1] = position_tmp[1] + length_step
        elif face_to == "s":
            position_tmp[1] = position_tmp[1] - length_step
        else:
            raise Exception()
    except:
        continue

# 输出坐标
print("{:},{:}".format(position_tmp[0], position_tmp[1]))
