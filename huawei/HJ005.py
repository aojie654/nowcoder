# encoding=utf-8
"""
HJ5 进制转换
"""

def result_append(result_list, elem_tmp):
    """
    Append incoming string with format to list
    """
    result_list.append(elem_tmp)

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
                num_tmp = int(input_str, 16)
                result_append(result_list=result_list, elem_tmp=num_tmp)
            else:
                raise EOFError()
        except EOFError:
            input_flag = False

    # print string in result_list
    for elem_tmp in result_list:
        print(elem_tmp)
