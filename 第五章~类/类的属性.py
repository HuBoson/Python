# obj.__dict__    对象的属性字典
# obj.__class__    对象所属的类
# obj.__name__     类的名字
# obj.__module__  类所在的模块__main__
# class.__bases__    类的父类元组(有可能有多个，系统默认为元组)
# class.__base__    类的父类
# class.__mro__    类的层次结构
# class.__subclasses__()：  类的子类列表
# getattr():获取属性
# setattr():修改属性
# delattr():删除属性
#示例一：
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name): self.name = name

a=A()
b=B()
c=C('我叫胡柏松')
print('对象c的属性字典是:',c.__dict__)   # a和b的属性字典为空，c有字典信息
print('对象c的所属的类是:',c.__class__)   # 所属父类为C（大写）
print('C的父类元组是:',C.__bases__)   # 结果为A和B两个元组，因其是继承了A和B类
print('C的父类是:',C.__base__)   # 结果为A类，如果继承了N个父类，只显示第一个父类
print('C类的层次结构是:',C.__mro__)   # C类继承了A和B类，也会继承了object默认类
print('C类的子类列表是:',C.__subclasses__())   # C类没有子类，为空列表，A和B有C这个子类

