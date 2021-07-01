# encoding=utf-8
"""
HJ4 字符串分隔
"""

def result_append(string_tmp):
    """
    Append incoming string with format to list
    """
    result_list.append("{:0<8}".format(string_tmp))

if __name__ == '__main__':
    # Init input flag
    input_flag = True
    result_list = list()

    # process every input
    while(input_flag):
        str_result = ""
        try:
            # input string 
            input_str = input("")
            if (input_str!=""):
                while len(input_str) > 8:
                    string_tmp = input_str[:8]
                    result_append(string_tmp=string_tmp)
                    input_str = input_str[8:]
                else:
                    result_append(input_str)
            else:
                raise EOFError()
        except EOFError:
            input_flag = False

    # print string in result_list
    for elem_tmp in result_list:
        print(elem_tmp)
