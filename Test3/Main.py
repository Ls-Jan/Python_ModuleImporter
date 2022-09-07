
import os
from XJImporter import *
Import =XJImporter(globals()).Import
Import('./add','add')
Import('A/mul','mul')

if __name__=='__main__':
    print(add(50,-20))
    print(mul(14,17))
    os.system("pause")
    

if False:#这部分代码没有实际运行意义，唯一的价值就是让打包器pyinstaller能够知道哪些模块是需要打包进程序当中
    import A.mul
    import add

