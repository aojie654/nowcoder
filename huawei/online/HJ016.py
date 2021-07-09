# encoding = utf-8

"""
HJ16 购物单
"""

# 获取输入内容以空格分割后的列表
input_list = input().split()
# 获取总钱数和购买物品数量
money_s, num_t = int(input_list[0]), int(input_list[1])
# 初始化购物清单的字典
goods_dict = dict()
# 数据结构
"""
goods_dict = {
    # weight: [has_primary, [price, primary], [price, primary]]
    2: [True, [800, True], [500, True]],
    3: [True, [400, True]],
    5: [False, [400, False], [300, False]]
}
"""

#初始化最终结果
final_result = 0

# 输入 num_t 次
for counter_tmp in range(num_t):
    # 获取以空格分割的元素列表
    input_list = input().split()
    # 获取当前物件的价格
    price_t = eval(input_list[0])
    # 获取当前物件的权重
    weight_t = eval(input_list[1])
    # 获取主件属性
    primary_t = eval(input_list[2])
    # 当权重对应的元素不存在时初始化假设没有主件
    if weight_t not in goods_dict.keys():
        goods_dict[weight_t][0] = False
    # 当物件为主件时，更新权重已有主件
    if primary_t == 0:
        goods_dict[weight_t][0] = True
    # 赋值价格
    goods_dict[weight_t][1][0]= price_t
    # 赋值物件属性
    goods_dict[weight_t][1][1]= primary_t

# 遍历每个元素
for weight_t in goods_dict.keys():
    # 当前物件不包含主件时直接跳过
    if goods_dict[weight_t][0] == False:
        continue
    # 对当前权重中的每个物件进行价格累加
    for elem_t in goods_dict[weight_t]:
        pass