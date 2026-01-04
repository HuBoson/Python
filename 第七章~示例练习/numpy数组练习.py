import numpy as np
print(np.__version__)   # 查询当前numpy版本号
a=np.zeros((3,5))    # 创建一个3行5列的0数组
print(a,'%d byts'%(a.size*a.itemsize))    # 占内存的字节数据大小：size（每个字节）*itemsize(每个字节占用的内存空间)
# print(help(np.info(np.add)))     # 通过help查找某个需要的函数的功能和info介绍
print('**'*50)

a1=np.arange(10,50,2)    # 创建一个10-50的数组，间隔2
print(a1[::-1])        # 倒序排列

a2=np.nonzero([1,2,0,3,0,5,0,0,6,7,8])     # 查询不是0的数字
print(a2)   # 结果是(array([ 0,  1,  3,  5,  8,  9, 10]),)，a2数组中0的数字下标（没有2,4,6,7）
print('**'*50)

a3=np.random.random((3,5))  # 随机创建矩阵
print(a3.min())      # 矩阵中的最小值
print(a3.max())      # 矩阵中的最小值
print('**'*50)

a4=np.ones((5,5))           # 创建一个值为1的矩阵
print(a4)
print(np.pad(a4,pad_width=1,mode='constant',constant_values=0))   # 通过np.pad函数在原有矩阵上增加一圈（pad_width=1）,值为0

a5=np.array([[1,3,44,33,22],
            [2,32,67,89,55],[4,7,12,34,66]])
a5_x=a5.max()
a5_y=a5.min()
print(a5[a5[:,1].argsort()])   # 数组中按列，下标1的顺序排列
# print(a5_x)
# print(a5_y)
# print(a5,(a5-a5_y)/(a5_x-a5_y))   # 做归一化处理
print('**'*50)

a6=np.random.randint(0,10,9)  # 从0-10随机生成9个数
a7=np.random.randint(0,10,9)
print(a6,a7)
print(np.intersect1d(a6,a7))   # 通过intersect1d找出相同的值

start_date = np.datetime64('2025-10-01')
end_date = np.datetime64('2025-11-01')  # 结束日期设为11月1日，arange不包括结束日期
a8 = np.arange(start_date, end_date, dtype='datetime64[D]')  # 生成一个月的数组
print(a8)
print('**'*50)

a9=np.random.uniform(0,9,10)   # 从0-9均匀的随机10个随机浮点数
print(np.ceil(a9))     #  将这些随机数向上取整
print(np.floor(a9))   #  将这些随机数向下取整

np.set_printoptions(threshold=np.inf)  # 当数据量太大时，改变“np.inf”为数字时，可以按数字显示的打印结果的行数或列数
a10=np.zeros((15,20))
print(a10)
print('**'*50)

a11=np.arange(9).reshape((3,3))  # 创建了一个3x3的数组，包含从0到8的整数。
for index,value in np.ndenumerate(a11):  # 枚举数组中的每个元素及其对应的索引下标
    print(index,value)
print('**'*50)

a12=np.array([1,3,1,2,3,1,4,6,7,5,6])
n=3
print(a12[np.argpartition(-1*a12,n)[:n]])    # argpartition统计数组中最大3个数字（n）
print('**'*50)
print(np.bincount(a12))   #  np.bincount从0-最大数，统计每个数字出现的次数

a13=np.random.randint(0,10,(4,4,4)) # 创建一个四维数组
# print(a13)
res=a13.sum(axis=(-2,-1))  # 通过轴，将最后2维的数组求和
print(res)
print('**'*50)

a14=np.arange(25).reshape((5,5))
print(a14)
a14[[0,1]]=a14[[1,0]]      # 将数组中前面两组进行了位置交换
print(a14)