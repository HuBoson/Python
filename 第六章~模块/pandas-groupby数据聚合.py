from tokenize import group
"""
Groupby(分组的列名或行名):主要应用给具有共同属性的行或列的数据进行分组,.agg()函数可以对每组单独和同时计算多种不同的数据或查看
"""
import numpy as np
import pandas as pd
import seaborn as sns
# groupby将新增的列或行对象融合后,通过numpy函数进行计算

period=pd.date_range('2025-01-01',periods=10000,freq='D')
df=pd.DataFrame(np.random.randn(10000,4),columns=['Data1','Data2','Data3','Data4'],index=period)
print(df.head(),'.head查看头部前面默认的5组数据,挂号填数字后,显示对应行数')
print('* '*50)
df['group1']=np.random.choice(['A','B','C','D'],size=10000)   # 生成数据,后面做聚合运算
print(df.tail(),'查看尾部的默认5行数据')
print('* '*50)
grouped=df.groupby('group1')        # 使用.groupby()函数以group1列为基准进行分类,重要知识点!
print(grouped.size(),type(grouped),'为groupby对象,用.size查看分别有多少组数量的A或B,C,D')
print('* '*50)
print(grouped.sum(),'按group1的ABCD四组分类求和')
print('* '*50)
print(grouped.max(),'求出每组的最大数')
print(grouped.mean(),'求出每组的平均数')
print('* '*50)
print(grouped.describe(),'求出每组的,差值,均值等整体数据特征概览')
print('* '*50)
print(np.transpose(grouped.describe()),'使用np.transpose()将数据从横向转向纵向表格显示')   # 常用功能
print('* '*50)
print(grouped.get_group('A').head(),'.get_group(函数)查看某个标签的数据')
print('* '*50)
# 双重Group
df['group2']=np.random.choice(['Python','C++','Java'],size=10000)
# print(df.tail())
grouped=df.groupby(['group1','group2'])    # 多组分类
print(grouped.size(),'多组分类后的size')
print('* '*50)
print(grouped.agg([np.mean,np.std,np.max,np.min]),'.agg函数列表传入可以自定义聚合,分类汇总,查看的数据元素')
print('* '*50)
print(grouped.agg({'Data1':np.mean,'Data2':np.sum}),'.agg字典传入列名查看该列元素')