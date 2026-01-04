# 多态方式调用函数，只要有共同的def函数名称（eat）就可以调用，与对象、数据类型、继承关系等无关
# 示例：三个类中都有一个相同的函数名称eat
class Person():
    def eat(self):
        print('人吃饭')

class Cat():
    def eat(self):
        print('猫吃鱼')

class Dog():
    def eat(self):
        print('狗吃骨头')

def fun(obj):    # obj是函数的默认形参
    obj.eat()     # 通过obj对象调用三个类同名函数eat的方式就形成了多态

# 创建对象
per=Person()
cat=Cat()
dog = Dog()
# 多态方式调用函数，只要有共同的函数名称（eat）就可以调用，与对象、数据类型、方法等无关
fun(per)
fun(cat)
fun(dog)