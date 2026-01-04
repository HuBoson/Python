"""
import+模块名称[as别名]：模块名称过长时可以取as别名代替，使用模块中的函数或变量时，模块名打点调用，同名不会覆盖
from+模块名称import变量/函数/类/*:导入模块中具有同名变量和函数，后导入的会将之前导入的进行覆盖，*结尾代表调用全部元素(容易与程序冲突,不常用)
包：__init__.py文件的文件夹（目录），可以避免模块名称相互冲突的问题，无须打点，可以直接调用！

if __name__ == '__main__':一般函数设定在主程序之前,方便其他文件调用,函数执行在主程序下面,防止被其他文件调用或每次启动程序时导致错误,不影响本身文件脚本的运行.

"""
# 以下几种不同的导入方式次，__init__文件只会导入一次
import admin.study as a  # admin是包名，study是模块名，a是通过as取的别名
a.info()                 # 调用时admin这个包下面的__init__文件自动调用执行

print('_'*50)
from admin import study as b  # from包名import模块名，b是通过as取的别名
b.info()                       # 不会重复执行__init__文件的内容，info是admin包里面的study模块函数名称

print('_'*50)
from admin.study import info  # from包名.模块名import函数/变量等，info是admin包里面的study模块函数名称
info()                        # 无须打点，直接调用

print('_'*50)
from admin.study import *    # from包名.模块名import*
print(name)                  # 无须打点，直接调用，可以取模块里面的任意元素

