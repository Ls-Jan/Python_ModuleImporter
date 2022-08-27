import os

import Tool



def Add_n(*args):
    rst=0
    for val in args:
        rst=Tool.Add_2(rst,val)
    return rst




