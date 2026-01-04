# 类的属性默认为object，是所有类直接或间接的父类，
# __init__()： 初始化方法
# __str__()：  用于对象的描述，返回值是str类型，默认输出对象的内存地址
# 类的方法重写：只调用重写后的参数，但重写的名字与父类相同
# 类的属性修改
class Student():
    def __init__(self,name,gender):
        self.name = name
        self.__gender=gender     # 没双下划线，类的内部、外部、及子类都可以访问
    def __str__(self):
        return'通过返回字符串的方式重写def方法'
    # 使用@property 修改方法，将方法转成属性使用，可以查看，不能修改属性，只能通过下面setter来修改
    @property
    def gender(self):
        return self.__gender
    # 使用setter 将gender属性设置为可写属性
    @gender.setter
    def gender(self,value):
        if value != '男'and value!='女':
            print('性别有误，将修改成女')
            self.__gender = '女'
        else:
            self.__gender = value

 # 创建对象
stu=Student('胡柏松','男')
print(stu)                                       # 结果与默认print(stu.__str__()）一样
print(stu.name,'性别是:',stu.gender)              # 结果 gender为男
stu.gender=''                                    # 需做赋值操作，调取第12行值
print(stu.name,'的性别是：',stu.gender)           # 结果 gender为女，此处是调用第8行代码执行