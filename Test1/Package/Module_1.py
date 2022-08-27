import os
from XJImporter import XJImporter
Import=XJImporter(globals()).Import
Import('Module_2')






def Func():
    print(f'【调用了Func函数】')
    print(f'【Module_2.name = "{Module_2.name}"】')
    










if __name__=='__main__':
    Func()
    os.system('pause')
    
    
    