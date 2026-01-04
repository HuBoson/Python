import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei']   # 解决中文乱码,指定默认字体
plt.rcParams['axes.unicode_minus']=False     #  解决负号'-'显示为方块的问题
'''
pandas可以根据DataFrame的日期和股价自动对应x和y轴,通过调用df.plot(刮号内可设置线粗细,颜色,title,图片大小,x,y轴名称等相关参数)
快速生成图片,比matplotlib更方便,但多图布局和多轴绘图需要结合 Matplotlib 来实现
'''

# np.random.seed()      # 固定随机数种子,保证每次生成的随机数相同
# a=np.random.standard_normal((30,2)).round(2)
# df=pd.DataFrame(a,columns=['Data1','Data2'])
# print(df.head())
# dates=pd.date_range(start='2025-01-01',periods=len(a),freq='D')   # periods参数指定生成多少个时间点,长度按表格最长设定
# df.index=dates
# print(df.head())
# print('* '*50)
# df.plot()    # DataFrame.plot() 函数整体可视化
# df.plot(figsize=(8,6),title='number',style='o--')    # 设置图片大小,title名称,style线的样式等
# df['Data1'].plot(figsize=(8,5),ylim=(-2,2))   # 也可以单独绘制某一个Series,xlim和ylim可以设定x和y轴的最大和最小值,如果设定ylim=[np.min(df.Data2)*1.2,np.max(df.Data2)*1.2]的方式不管数据如何变化都能大1.2倍的全部显示
# df[['Data1','Data2']].plot(subplots=True,figsize=(8,6),sharex=True,sharey=True)   # subplots=True子图分开显示出设定的数据表格数量,

# 绘制直方图
# df.hist(figsize=(10,8),bins=9)      # 绘制直方图,bins修改直方图的柱子精度显示
# 绘制散点图
# df.plot.scatter(x='Data1',y='Data2',kind='scatter',figsize=(8,6))  # 常用画股价的相关性,x轴以Data1为基准,y轴以Data2为基准,kind参数设置散点图\柱状图等风格
# df.cumsum().plot(figsize=(8,6))     # 数据进行运算后再绘制图形
# df.plot(style=['-','m--'],figsize=(8,6))    # 修改字母更改颜色和线的样式都可以个性化修改
# df['Data2']=df['Data2']*100             # Data2乘100后,两个数据图形相差太大,导致无法在同一张图显示,模仿两只股价相差太大又需要放在一张图中分析使用
# df.plot(grid=True,figsize=(10,7),secondary_y='Data2')   # 设定大数据以Data2为Y轴显示(相当于2个y轴)secondary_y='Data2'就可以在同一张图中显示

# 在图中显示中文字的解决方案
# data=np.random.standard_normal((100000,2))
# df=pd.DataFrame(data,columns=['Data1','Data2'])
# print(df.head())
# plt.rcParams['font.sans-serif']=['SimHei']   # 解决中文乱码,指定默认字体
# plt.rcParams['axes.unicode_minus']=False     #  解决负号'-'显示为方块的问题
# df[(df.Data1>2)&(df.Data2<-2)].plot(x='Data1',y='Data2',kind='scatter',figsize=(8,6),title='中文标题')
# plt.show()  # 在jupyter可以不用此函数就可以调用

# 结合 Matplotlib 来实现子图布局和多轴绘图
# 创建一些示例数据
data = {
    'A': range(10),
    'B': [x**2 for x in range(10)],
    'C': [x**3 for x in range(10)]}
df = pd.DataFrame(data)
# 创建一个包含两个子图的图形
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))
# 在第一个子图上绘制 A vs B 的折线图
df.plot(x='A', y='B', ax=axes[0], title='A vs B')
# 在第二个子图上绘制 A vs C 的散点图
df.plot.scatter(x='A', y='C', ax=axes[1], color='red', title='A vs C')
# 调整子图之间的间距
plt.tight_layout()
# 显示图形
plt.show()

