#encoding=utf-8

"""
HJ7 取近似值
"""

number_t = input()

try:
    if number_t != "":
        number_t = float(number_t)
        if number_t - round(number_t,0) < 0.5:
            number_t = round(number_t,0)
        else:
            number_t = round(number_t,0) + 1
        print("{:}".format(int(number_t)))
    else:
        raise EOFError()
except EOFError:
    pass
