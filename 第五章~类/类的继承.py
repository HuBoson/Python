# 子类可以继承N个父类，父类也可以拥有N个子类，用逗号分开
# 如果一个类没有继承任何类，默认继承的是object
# 继承语法结构：Class+类名(父类1，父类2...N)：
## 注意调用self参数时，需用self打点调用
# 子类可以继承父类的方法及参数，父类参数不能适合子类需要时，子类可以重写自己的方法或参数，但方法名称必须与父类一致，也可以用suer()或“父类名.__init__”调用父类参数方法
# 示例一：一个父类多个子类
class Person:   # 默认object，父类
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f'大家好，我是{self.name},我今年{self.age}岁')   # 需用self打点调用

# 子类一：
class Student(Person):      # 继承Person父类
    def __init__(self, name, age, stuno):
        super().__init__(name, age)          # 使用super调用父类的__init__参数
        self.stuno = stuno                   # 子类与父类不一样的参数
    def show(self):                           # 调用父类方法进行修改或增加参数
        super().show()                       # 用super()调用父类参数，再增加下行代码参数
        print(f'我来自深圳，我的学号是:{self.stuno}')    # 需用self打点调用

#子类二：
class Doctor (Person):        # 继承Person父类
    def __init__(self, name, age, deapartment):
        super().__init__(name, age)          # 使用super调用父类的__init__参数
        self.deapartment = deapartment           # 子类与父类不一样的参数
    def show(self):                               # 不用super()调用父类参数，直接修改父类方法或增加参数
        print(f'我是一名医生，我的名字是{self.name},我今年{self.age},我的工作科室是{self.deapartment}')

# 创建对象
stu=Student('胡柏松',35,'1001')
stu.show()   # 调用子类自己的show方法
doctor=Doctor('张一一',42,'外科')
doctor.show()   # 调用子类自己修改过的show参数

# 示例二：多个父类，子类的调用不能用super(),直接用父类名打点调用
print('*'*50)

class FatherA():         # 父类一
    def __init__(self,name):
        self.name = name
    def showA(self):
        print('父类A的方法')

class FatherB():              # 父类二
    def __init__(self,age):
        self.age = age
    def showB(self):
        print('父类B的方法')

class Son(FatherA,FatherB):      # 子类
    def __init__(self,name,age,gender):
        FatherA.__init__ (self,name)             # 只能用父类名打点调用参数，多父类的情况下不能super()调用
        FatherB.__init__ (self,age)              # 需用self打点调用
        self.gender = gender

son=Son('胡柏松',35,'男')
son.showA()
son.showB()
