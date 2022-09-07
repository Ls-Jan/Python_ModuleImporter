
__version__='1.0.1'
__author__='Ls_Jan'


import sys
import os
class XJImporter:#专治各种不服
    '''
        模块导入，用于导入模块，尤其是相对路径下的导入。
        已经解决“脚本打包成程序后程序无法运行”的问题。
    '''
    def __init__(self,context):
        '''
            context为上下文环境，在创建对象时直接传入globals()即可
        '''
        self.__context=context
    def Import(self,module,args=None):
        '''
            module为模块名所在路径(不需要.py后缀)，支持相对路径：
                导入上一级名为M的模块，那么module='../M'
                导入目录A下的名为M的模块，那么module='A/M'
            args为从module中导入的变量名或者变量名列表：
                如果args为空，那么仅导入模块module
                如果args不为空，那么将导入模块module中的变量
                
            例子：
                Import('M')：导入模块M。【类似于import M】
                Import('M','info')：导入模块M中名为info的变量。【类似于from M import info】
                Import('M',('info','func'))：导入模块M中名为info和func的变量。【类似于from M import info,func】
                Import('M','*'):导入模块M中所有内容。【类似于from M import *】
                Import('../M')：导入上级目录中的模块M
                Import('./M')：导入当前目录下的模块M。等同于Import('M')
                Import('A/M')：导入A目录下的模块M
            注：
                ①、请不要传入各种奇奇怪怪的值，我可没做好各种极端情况的预防工作
                ②、import失败必然会抛出异常，这没得洗的。请注意自己的代码规范
                ③、经常出现“鸡与蛋的先后问题”。请将该文件复制到要跨目录导入的脚本所在的目录下
        '''
        name=self.__context['__name__']#获取上下文环境的相对路径__name__
        stack_name=name.split('.')
        stack_name.pop()
        if(len(stack_name)==0):
            stack_name=['__main__']
        for key in module.split('/'):
            if(key=='.'):
                continue
            elif(key=='..'):
                if(stack_name[0]=='__main__'):#跑飞了，采用修改sys.path的方式导入模块(老方法)
                    return self.__Import_Absolute(module,args)
                else:
                    stack_name.pop()
                    if(len(stack_name)==0):
                        stack_name=['__main__']
            else:
                stack_name.append(key)
        if(stack_name[0]=='__main__'):
            name=stack_name.pop(0)
            module='.'.join(stack_name)
        else:
            module=stack_name.pop()
            name='.'.join(stack_name+['XXX'])#因为相对路径导入并不关心其文件名到底叫啥，甚至连它存不存在都不关心，所以瞎取得了
        return self.__Import_Relative(name,module,args)
        
    def __Import_Absolute(self,module,args):#采用绝对路径导入模块(旧方法，仅适用于脚本运行)
        absolutePath=os.path.split(self.__context['__file__'])[0]#调用该函数的文件所在的路径(绝对路径)
        relativePath,module=os.path.split(module)#模块所在目录(相对路径)、模块名
        path=os.path.join(absolutePath,relativePath)#模块所在路径(绝对路径)
        
        sys.path.append(path)#将路径临时加入到系统列表中
        if(args):
            if(type(args)==str):
                exec(f'from {module} import {args}',self.__context)
            else:
                exec(f'from {module} import {",".join(args)}',self.__context)
        else:
            exec(f'import {module}',self.__context)
        sys.path.pop()#移除临时加入的路径

    def __Import_Relative(self,name,module,args):#采用相对路径导入模块
        node='.' if name!='__main__' else ''#如果是主脚本路径下的话就不需要.导入
        context={'__name__':name}
        if(args):
            if(type(args)==str):
                exec(f'from {node}{module} import {args}',context)
            else:
                exec(f'from {node}{module} import {",".join(args)}',context)
        else:
            if(node):
                exec(f'from . import {module}',context)
            else:
                exec(f'import {module}',context)
        temp=self.__context['__name__']#临时保存一下
        self.__context.update(context)
        self.__context['__name__']=temp#恢复回去
