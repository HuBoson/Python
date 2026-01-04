# 赋值变量：指向的内存地址和空间是相同的
# 浅拷贝copy：子对象的内存地址和空间是相同的，但拷贝后的对象（变量）的内存地址不一样
# 深拷贝deepcopy: 递归拷贝所有源对象、拷贝后的对象和子对象，都不一样
# 示例：
class Cpu:
    pass
class Disk:
    pass
class Computer():
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk
cpu=Cpu()
disk=Disk()
com = Computer(cpu,disk)
# 变量（对象）的赋值：不会增加内存空间地址，两个变量是同一个地址
com1=com
print(com,'子对象的内存地址:',com.cpu,com,disk)
print(com1,'子对象的内存地址:',com1.cpu,com1,disk)

# 浅拷贝copy:
import copy    # 导入拷贝模块
print('___'*50)
com2=copy.copy(com)      # com2是新产生的对象，它的子类是cpu和disk不变
print(com,'子对象内存地址:',com.cpu,com,disk)
print(com2,'子对象内存地址:',com2.cpu,com2,disk)

# 深拷贝deepcopy:
import copy    # 导入拷贝模块
print('___'*50)
com3=copy.deepcopy(com)      # com2是新产生的对象，它的子类是cpu和disk不变
print(com,'子对象内存地址:',com.cpu,com,disk)
print(com3,'子对象内存地址:',com3.cpu,com3,disk)
