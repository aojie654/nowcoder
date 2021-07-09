# encoding=utf-8
"""
HJ3 明明的随机数
"""

# Initial input list
input_list = list()

# Initial input flag and counter
input_flag = True
list_tmp = list()

while input_flag:
    # input length at 1st line
    try:
        len_tmp = input()
        if (len_tmp != ""):
            # get the length
            len_tmp = int(len_tmp)
            # initial a list 
            list_elem_tmp = list()
            for counter_tmp in range(0, len_tmp):
                # get every element for this list
                elem_tmp = input()
                if elem_tmp !="":
                    elem_tmp = int(elem_tmp)
                    if elem_tmp not in list_elem_tmp:
                        list_elem_tmp.append(elem_tmp)
                    else:
                        pass
                else:
                    pass
            # Append this list to list of list
            list_elem_tmp.sort()
            list_tmp.append(list_elem_tmp)
        else:
            raise EOFError("")
    except Exception:
        # Go to end if no length input
        input_flag = False

# print every elem
for list_elem in list_tmp:
    for elem_tmp in list_elem:
        print(elem_tmp)