# encoding = utf-8

"""
HJ18 识别有效的IP地址和掩码并进行分类统计
"""

# 长度7位，分别对应A, B, C, D, E, 错误IP/掩码, 私有IP 的数量
result_list = [0, 0, 0, 0, 0, 0, 0]

def judge_ip(ip):
    try:
        # 获取4个地址段
        ip_split = ip.split(".")
        ip_addr1 = int(ip_split[0])
        ip_addr2 = int(ip_split[1])
        ip_addr3 = int(ip_split[2])
        ip_addr4 = int(ip_split[3])
        if ip_addr3 in range(0, 256) and ip_addr4 in range(0, 256):
            # 地址段1为0或者127时跳过
            if (ip_addr1 in [0, 127]):
                pass
            # 判断私有地址
            elif ((ip_addr1 == 10) or
                  ((ip_addr1 == 172) and (ip_addr2 in range(16, 32))) or
                  ((ip_addr1 == 192) and (ip_addr2 == 168))):
                # 增加私有地址数量
                result_list[6] = result_list[6] + 1
            # 判断 A 类地址
            elif (ip_addr1 in range(1, 127)):
                # 增加A类地址数量
                result_list[0] = result_list[0] + 1
            elif (ip_addr1 in range(128, 192)):
                # 增加B类地址数量
                result_list[1] = result_list[1] + 1
            elif (ip_addr1 in range(192, 224)):
                # 增加C类地址数量
                result_list[2] = result_list[2] + 1
            elif (ip_addr1 in range(224, 256)):
                # 增加D类地址数量
                result_list[3] = result_list[3] + 1
            else:
                # 增加错误地址/掩码数量
                raise Exception
        else:
             raise Exception
    except Exception:
        # 出现异常，增加错误地址/掩码数量
        result_list[5] = result_list[5] + 1
    return

def judge_mask(mask):
    position_0 = -1
    # 获取.分割后的ip段列表
    mask_split = mask.split(".")
    # 初始化二进制字符串
    mask_binary = str()
    # 对掩码每个地址段进行遍历拼接
    for mask_addr in mask_split:
        # 拼接去掉开头0b的二进制部分
        mask_addr_binary = "{:0>8}".format(bin(int(mask_addr))[2:])
        mask_binary = mask_binary + mask_addr_binary
    # 查询第一个0出现的位置
    position_0 = mask_binary.find("0")
    # 当存在0时
    if position_0 != -1:
        # 获取第一个0开始到结束的长度
        mask_tail = mask_binary[position_0:]
        # 如果有 1 存在 0 之后, 即非法掩码+1
        if "1" in mask_tail:
            result_list[5] = result_list[5] + 1
        else:
            pass
    else:
        pass

if __name__ == "__main__":
    flag_input = True
    while flag_input:
        try:
            # 获取输入, 以 "~" 分割存放至列表
            input_list = input().split("~")
            # 获取IP
            ip = input_list[0]
            judge_ip(ip)

            # 获取掩码
            mask = input_list[1]
            judge_mask(mask)
        except Exception:
            flag_input = False
    
    for elem_tmp in result_list:
        print(elem_tmp, end=" ")