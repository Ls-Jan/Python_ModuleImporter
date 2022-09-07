
from XJImporter import *
Import =XJImporter(globals()).Import
Import('../add','add')



def mul(a,b):
    if(b<0):
        a,b=-a,-b
    rst=0
    for i in range(b):
        rst=rst+a
    return rst

if __name__=='__main__':
    print(mul(10,20))
    os.system("pause")
    
    