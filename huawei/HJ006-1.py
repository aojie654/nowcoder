# encoding=utf-8

"""
HJ6 质数因子
"""

number_t = int(input())
# number_t = 2000000014
list_vars = list()
var = 2
list_varz = [2]


def is_z(num_tmp):
    for elem_tmp in list_varz:
        if num_tmp % elem_tmp == 0:
            break
        else:
            continue
    else:
        list_varz.append(num_tmp)


if __name__ == '__main__':
    while(number_t != 1):
        # print("Current {:}".format(var))
        if (number_t % var) == 0:
            number_t = number_t / var
            list_vars.append(var)
            var = 2
        else:
            var = var + 1
            if var not in list_varz:
                is_z(var)
    print("{:}".format(list_varz))
    print("{:}".format(list_vars))
