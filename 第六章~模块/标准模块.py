"""
os模块：与操作系统和文件相关操作有关的模块
math模块:用于数学计算的模块,math.log.....
re模块：用于字符串正则表达式的模块
json：用于对高维数据进行编码和解码的模块
time：与时间相关的模块
datatime：与日期时间相关的模块，可以方便的显示日期并对日期进行运算
random模块：用于产生随机数的模块，有以下操作：
          seed(x):初始化一个固定的随机数种子，默认为当前系统时间
          random():产生一个(0.0,1.0)之间的随机小数，不含1
          randint(a,b):生成一个(a-b)之间的整数，含a和b
          randrange(m,n,k):生成一个(m-n)之间步长为K的随机整数，不含n
          uniform(a,b):生成一个(a-b)之间的随机小数，含a和b
          choice(seq):从序列中随机选择一个元素
          shuffle(seq):将序列seq中元素随机排列，返回打乱后的序列
"""
import random

random.seed(10)           # 设置随机数的种子
print(random.random())    # 产生一个(0.0,1.0)之间的随机小数，不含1的
print(random.random())    # 每次生成的不一样的随机数

print('_' * 50)
random.seed(10)           # 设置随机数的种子
print(random.randint(1,20))    # 生成一个(a-b)之间的随机整数，含a和b
for i in range(10):     # 执行10次
    print(random.randrange(1,10,3)) # m为1，n为10，步长k为3，执行时不含n
print(random.uniform(1,100))     # 随机小数，含a和b

print('_'*50)
lst=[i for i in range(1,10)]
print(random.choice(lst))     # 随机取出一个数
random.shuffle(lst)           # 随机排序，每次运行结果不一样
print(lst)
random.shuffle(lst)           # 随机排序，每次运行结果不一样
print(lst)


