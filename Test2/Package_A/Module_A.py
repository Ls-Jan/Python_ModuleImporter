import os

from XJImporter import XJImporter
Import=XJImporter(globals()).Import
Import('../Tool')




def Add_n(*args):
    rst=0
    for val in args:
        rst=Tool.Add_2(rst,val)
    return rst




if __name__=='__main__':
    print(Add_n(1,2,3,4,5,6))
    os.system("pause")
    