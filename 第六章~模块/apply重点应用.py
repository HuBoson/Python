import pandas as pd
import numpy as np
from numpy.ma.core import filled
"""
apply:允许使用自定义函数进行复杂的数据处理，包括条件逻辑、调用其他库函数等,处理效率比for快,比numpy向量化慢.
DataFrame.apply(func, axis=0): 对某个函数,每一列（默认）或每一行（axis=1）应用函数。  
Series.apply(func): 对Series中的每个元素应用函数。
"""
a=np.random.randn(9,6).round(2)
df=pd.DataFrame(a)
print(df,'通过ndarray构建DataFrame,这种方法要熟练掌握')
df.columns=['a','b','c','d','e','f']     # 创建列columns名称
df.index=dates=pd.date_range('20250101',periods=9,freq='D')   # freq也可以以周,月等
print(df,'给每列创建a,b,c,d,e,f名称,且将index更改为以日的时间列')
def square_fun(x):
    return x**2
df=df.apply(square_fun)               # 重点掌握常用的方法
print(df,'通过apply可以将函数的复杂多维向量化的运算到每个元素')
df=df.apply(lambda x:x**2)
print(df,'通过apply,也可以采用lambda匿名函数运算后,向量化的运算到每个元素')
# def find_min(x):
#     return x.min()
# df=df.apply(find_min,axis=0)     # 默认axis=0按列,找出最小值
# print(df,'通过apply,向量化的按行找到最小值')
# df=df.apply(lambda x:x.max(),axis=1)   # 也可以采用lambda匿名找出最大值
print(('* ')*50)
df=df.sort_index(axis=0,ascending=False)   # 按index排序,ascending为True升序,为False降序
print(df,'按列或按行排序,注意是按index和column标签名称排序')
print(df.sort_values(by='b',ascending=False),'通过设定b标签,按某列或某行的values值进行升或降的排序')
print(('* ')*50)
print(np.sqrt(df),'通过numpy给dataframe每个元素开根号运算')                  # pandas非常强大特点之一,容错性高,且大部分的numpy的函数都可以调用
print(('* ')*50)
print(np.sqrt(df).sum(),'通过numpy给dataframe每个元素sum求和运算,默认按列')     # 缺失数据(Nan空值)对pandas操作没有影响
print(('* ')*50)

# 处理空值示例:
df_nan=pd.DataFrame([np.random.randn(4),[1.5,np.nan,np.nan,5],[4.5,np.nan,np.nan,np.nan],[1.5,np.nan,2.5,np.nan]])
df_nan.columns=['a','b','c','d']
print(df_nan.isnull(),'采用isnull函数判断哪些是空值')
print(df_nan,'创建一个有空值的DataFrame')
print(('* ')*50)
print(df_nan.dropna(axis=0),'采用dropna函数按行或列删除空值,只保留无空值的整列或整行,有空值会全部删除')
print(('* ')*50)
print(df_nan.fillna(0),'采用fillna函数填充空值,可以按平均值,0或1等不同值进行填充') # 常用功能,可以用ffill向前或bfill向后填充
# 数据预处理：提前填充或删除缺失值，如用前一日数据填充（fillna(method='ffill')）或用均值填充，确保窗口计算的稳定性

