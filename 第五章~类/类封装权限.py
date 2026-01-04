
# 类是通过对属性或方法添加单下划线、双下划线及首尾双下划线来对类进行封装
# 注意调用self参数时，需用self打点调用
class Student():
    def __init__(self,name,age,gengder):   # name,age为形参，也是类里面的一个局部变量
        self._name = name       # “_"单下划线命名的实例属性变量为受保护，只能本类和子类访问
        self.__age = age        # “__"双下划线命名的实例属性变量为私有，只能本类访问
        self.gender=gengder     # 没有下划线为普通实例属性，类的内部、外部、及子类都可以访问

    def _fun1(self):          # “_"单下划线命名的方法
        print('“_"单下划线命名的方法，子类和本身可以访问')

    def __fun2(self):  # “__"双下划线命名的方法
        print('“_"双下划线命名的方法，只有本身可以访问')
        

    def fun3(self):      # 没有下划线命名的方法
        self._fun1()     # 子类和本身可以访问
        self.__fun2()    # 只有本身可以访问
        print(self._name)   # 子类和本身可以访问
        print(self.__age)    # 只有本身可以访问

 # 创建对象
stu=Student('胡柏松',35,'男')
print(stu._name)
 # 私有实例属性和方法可以用下面方式调用
print(stu._Student__age)
stu._Student__fun2()