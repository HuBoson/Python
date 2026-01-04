import matplotlib.pyplot as plt
import numpy as np
from numpy.ma.core import cumsum
# import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei']   # 解决中文乱码,指定默认字体
plt.rcParams['axes.unicode_minus']=False     #  解决负号'-'显示为方块的问题
# plt.show()  # 在jupyter可以不用此函数就可以调用
"""
准备x和y轴数据(如:对应日期与股价)绘制图形,可以设置图形的title,线style,颜色等参数,每个步骤需单行plt.打点调用相应设置
plt.polt():绘制图形,刮号输入x轴和y轴;pandas下的绘制无需提供x和y轴的原因是DataFrame的数据具有x和y轴
plt.show():显示图形,IDE中必须调用才能显示绘制图,如pycharm
plt.figure():生成图形尺寸,挂号里开填入图片的大小尺寸
plt.title(): 确定图片标题,挂号里输入标题名字
plt.xlabel(): 确定图片的x轴名称
plt.ylabel(): 确定图片的y轴名称
plt.legend(): 显示图例位置(创建图例有设置图例才能调用显示),如:一只股价一个股价图例线,如图中有多只股价多条股价线
plt.scatter():绘制散点图
plt.gird(True):绘制底色有网格显示的效果
plt.subplot(): 绘制子图
plt.bar(): 绘制柱状图
"""
# 添加图例和设置线型\颜色
# plt.plot([1,2,3,4],[2,4,6,8],'r--',linewidth=1.0,label='line')            # 第一个列表是x轴的的数据,第二个列表是y轴的数据,'r--'设置线的style风格,label='line'增加图例名称,linewidth设置线宽
# plt.xlabel('Number')               # xlabel确定x轴的名称
# plt.ylabel('yyy')               # ylabel确定y轴的名称
# plt.legend(loc='upper left')    # legend()显示上面设置的图例label='line',loc='upper left'指定图例显示的位置左上方
# plt.ylim(0,10)                   # 设置y轴的显示范围以0-8显示
# plt.xlim(0,2.5)                     # 设置x轴的显示范围以0-10显示
# print(plt.show ())

#
# import seaborn as sns    # 导入seaborn模块效果会有所提升
# # 绘制多条线的显示
# # t=np.arange(0,5,0.2)
# # plt.plot(t,t,'r--',t,t**2,'b',t,t**3,'g')   # t,t,'---'为绘制的线,t,t**2,'bs'为绘制的线,t,t**3,'g^'为绘制的线
# # print(plt.show ())

# 调整图片和坐标值大小
# np.random.seed(10)   # # 固定随机数种子,保证每次生成的随机数相同
# y=np.random.standard_normal(20)       # 生成y轴数据
# x=range(len(y))                       # 生成x轴数据
# plt.figure(figsize=(8,6))              # plt.figure确定图片大小
# plt.plot(x,y)                   # x是序号,默认时,不提供x也能绘制出图片
# print(plt.show ())
# plt.plot(y.cumsum())                  # 可增加运算后的数据图形对比
# print(plt.show ())
#
# 分别编写绘制图命令,输出在同一张图内
from matplotlib import style
# style.use('ggplot')           # matplotlib下的一种灰底色块的style模版
# x=[1,5,10]
# y=[2,8,16]
# x2=[10,5,1]
# y2=[9,20,7]
# plt.figure(figsize=(8,6))        # 生成图片且设置大小
# plt.plot(x,y,linewidth=1,label='line1')               # 绘制line1线在图片上,label='line1'为图例名称
# plt.plot(x2,y2,linewidth=2,label='line2')           # 绘制line2线在图片上,label='line2'为图例名称
# plt.title('TWO line plot')                                #  图片标题
# plt.xlabel('Y axis')                                      # 设定y轴名称
# plt.ylabel('X axis')                                # 设定x轴名称
# plt.legend()
# plt.legend(loc='upper left')          # 显示图例在左上角
# plt.grid(True)                         # 增加网格线
# print(plt.show ())

# 绘制散点图plt.scatte()
# x=[1,5,10,10,5,4,6,9,12]
# y=[2,8,16,12,10,7,8,13,15]
# plt.figure(figsize=(8,6))
# plt.scatter(x,y,s=50,c='r',marker='o',alpha=0.5)
# plt.title('Scatter plot')
# plt.xlabel('X axis')
# plt.ylabel('Y axis')
# plt.grid(True)
# print(plt.show ())

# 两维图形绘制
# np.random.seed(2000)
# y=np.random.randn(20,2).cumsum(axis=0)   # 生成的20行2列的ndarray数据结构,cumsum(axis=0)按列求和
# plt.figure(figsize=(7,4))
# plt.plot(y,linewidth=1.5)
# plt.grid(True)
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.title('Two dimensional plot')
# plt.plot(y[:,0],linewidth=1.5,label='line1')   # 设定第一列20行数据都需要,0是从第一行开始画线,同时可以设定该线的label名称以便分辨是哪条线
# plt.plot(y[:,1],linewidth=1.5,label='line2')     # 设定第二列20行数据都需要,1是从第二行开始画线
# plt.legend(loc=0)
# print(plt.show ())

# 数据差异很大的两个数据绘制在同一张图的方法:
# np.random.seed(2000)
# y=np.random.randn(20,2).cumsum(axis=0)   # 生成的20行2列的ndarray数据结构,cumsum(axis=0)按列求和
# y[:,0]=y[:,0]*100      # 第一列的数据增加了100倍会导致line2失真,模仿两只股票价格很大,需要放在一起对比时用
# fig, ax = plt.subplots(figsize=(10,6))     # 使用plt.subplots()创建子图的方法,绘制一个具有相同x轴,不同y轴的图形,返回fig对象和ax一个坐标轴对象
# plt.plot(y[:,0],linewidth=1.2,label='line1')
# plt.xlabel('X')
# plt.ylabel('Y')     # 第一列Y轴在左侧
# plt.legend(loc=8)
# plt.title('Two dimensional plot')
# ax2=ax.twinx()           # 第二列的数据复制了上面子图的第一数据的横坐标x轴
# plt.plot(y[:,1],'r--',linewidth=1.2,label='line2')
# plt.legend(loc='best')
# plt.ylabel('Y2')       # 第二列Y轴在右侧
# print(plt.show())

# 两行一列横向绘制两张子图
# np.random.seed(2000)
# y=np.random.randn(20,2).cumsum(axis=0)   # 生成的20行2列的ndarray数据结构,cumsum(axis=0)按列求和
# plt.figure(figsize=(8,6))
# plt.subplot(211)            # plt.subplot函数绘制两行一列的第一张子图
# plt.plot(y[:,0],linewidth=1.2,label='line1')
# plt.ylabel('Y')
# plt.title('Sub plot')
# plt.legend(loc='best')
# plt.subplot(212)              # plt.subplot函数绘制两行一列的第二张子图
# plt.plot(y[:,1],'r--',linewidth=1.2,label='line2')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend(loc='best')
# print(plt.show())

# 一行两列纵向绘制两张子图,其中一张为柱状图
# np.random.seed(2000)
# y=np.random.randn(20,2).cumsum(axis=0)   # 生成的20行2列的ndarray数据结构,cumsum(axis=0)按列求和
# plt.figure(figsize=(12,5))
# plt.subplot(121)        # plt.subplot函数绘制一行二列的第一张子图
# plt.plot(y[:,0],linewidth=1.2,label='line1')
# plt.grid(True)
# plt.legend(loc='best')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.title('1st Data set')
# plt.subplot(122)             ## plt.subplot函数绘制一行二列的第二张子图
# plt.bar(np.arange(len(y[:,1])),y[:,1],width=0.5,color='r',label='line2')     # 绘制柱状图,with为线宽设置,color为颜色设置,label为图例名称
# plt.grid(True)
# plt.legend(loc='best')
# plt.xlabel('Index')
# plt.title('2nd Data set')
# print(plt.show())

 #  绘制散点图:在分析股价相关性常用,用点的方法绘制
# y=np.random.standard_normal((1000,2))
# plt.figure(figsize=(10,6))
# plt.plot(y[:,0],y[:,1],'c.')    # 绘制散点图,c为颜色设置,'.'为散点样式设置
# plt.grid(True)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Pie plot图')
# print(plt.show())