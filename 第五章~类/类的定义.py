# 类的定义：class（“c”不能大写），类名称首字母必须大写，可以由类名+类属性+实例属性+实例方法+静态方法+类方法，语法结构组成
# 实例方法：必须自带self参数
# 动态方法：可以根据需要动态绑定或修改方法和属性，但仅限于当前对象或方法使用
# 类方法：采用装饰器@classmethod修饰
# 静态方法：采用装饰器 @staticmethod修饰
# 类的方法重写：只调用重写后的参数，但重写的名字与父类相同
# 类属性：在def函数外定义，实例属性是__init__初始化方法中打点
class Student():                # 类名Student好Class两个首字母需大写
    school='深圳市第一高级中学'     # 这里school定义在方法外，为类属性，也是变量
    # 定义在类中的函数，称为“方法”，会自带self参数，如下：
    # 1.初始方法：定义在__int__方法中，如果没有实例属性时可以不用此方法
    def __init__(self,name,age):   # name,age为形参，也是类里面的一个局部变量
        self.name = name       # 实例属性，将形参局部变量赋值给左侧
        self.age = age      # 实例属性，形参局部变量的名称也可以和实例属性相同
    # 2.实例方法：定义类的函数，自带一个self参数：
    def show(self): print(f'我叫：{self.name},今年：{self.age}岁了')
    # 3.静态方法：不自带self，使用装饰器@staticmethod修饰的方法：
    @staticmethod
    def sm():
        print('这个是静态方法，不能调用实例属性和实例方法')
    # 4.类方法：使用装饰器@classmethod修饰的方法：
    @classmethod
    def cm(cls):     # clss是class的缩写
        print('这个是类方法，不能调用实例属性和实例方法')
# 创建类的对象：
stu=Student('Boson',18)  # 为什么传了2个参数，因为__int__方法中有两个形参，self是自带参数，无需手动传入
print(stu.name, stu.age)            # 实例属性，使用对象名进行打点调用
# print(Student.school)             # 类属性，直接使用类名，打点调用
# stu.show()                        # 实例方法，使用对象名进行打点调用
# Student.sm()                      # @staticmethod静态方法,直接使用类名打点调用
# Student.cm()                      # @classmethod类方法,直接使用类名打点调用

# 可以创建多个对象
stu1=Student('胡柏松',28)
stu2=Student('张三',25)
stu3=Student('李四',38)
stu4=Student('王一一',25)

Student.school='深圳学校'    # 给类的类属性赋值
#将学生对象存储到列表中
lst=[stu,stu1,stu2,stu3,stu4]    # 列表中的元素是Student类型的对象
for item in lst:                 #item是列表中的元素，是Student类型的对象
    item.show()                  # 对象名打点调用实例方法

# 可以动态增加绑定实例属性，如下：
stu1.gender='男'
print(stu1.name,stu1.gender,stu1.age)   # 结果多了“男”的实例属性

# 也可以动态判定一个方法，如下：
def introduce():
    print('我是一个普通函数，我被动态绑定成st2对象的方法')
stu2.fun=introduce         # 赋值后，introduce就是stu2对象的方法
stu2.fun()     # 直接调用

