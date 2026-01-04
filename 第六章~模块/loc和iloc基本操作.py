import pandas as pd
import numpy as np
#通过字典构建DateFrame
dcit_date={'Date':pd.to_datetime('2025-12-13'),'Number':pd.Series([6,6,6,6]),
           'Course_name':pd.Series(['Python','Quant','Java','CFA']),'Company':'JCAQF'}
dt=pd.DataFrame(dcit_date)
print(dt,"字典构成的DateFrame")
print('* '*50)

# 通过numpy构建的DataFrame
array=np.random.randn(6,4)
df=pd.DataFrame(array)
print(df,'通过Ndarray构建的Dataframe,如果没有声明,默认的行index和列columns都是从0开始')
df=pd.DataFrame(np.random.randn(6,4),columns=['A','B','C','D'],index=['e','f','g','h','i','j'])
print(df)
print('* '*50)
# loc:通过标签索引,可以是行,也可以是列,选取的范围的前后都能选到,双闭区间
print(df.loc['f':'i'],['A'],'使用loc通过标签进行索引,从哪行开始到哪行结束的选择')
print(df.loc[['f','i'],['A']],'同时获取行和列的数据，行f-i和列A的数据') # loc基于label标签,如果只有一个索引则为行的index,行优先
# print(df['h'],'行不能通过index直接索引,会报错!但列可以(文字大小写需一致),一般采用loc')
print('* '*50)
# iloc:通过位置索引行或列,选取的范围的前面能选到,最后一个选不到,前闭后开
print(df.iloc[0:2,1:3],'通过iloc选择只能前闭后开,0:2是指行：第1-2行，1:3为列：第2-3列的元素')
