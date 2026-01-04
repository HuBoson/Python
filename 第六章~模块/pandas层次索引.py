import numpy as np
import pandas as pd
df=pd.Series(np.random.randn(5),index=[['a','a','b','b','b'],[1,2,1,2,3]])
print(df,'创建一个第一层level 0是a和b,第二层level 1是1,2,3数字的多层次表格')
print('* '*50)
print(df.index,'为MultiIndex多层次索引数据类型')
print('* '*50)
print(df['b'],'通过第一层level 0的a或b查找该层下的元素')
print('* '*50)
print(df.unstack(),'使用unstack()函数将数据重新排列')
print('* '*50)
print(df.unstack().stack(),'使用嗯stack()函数将数据取消重新排列')
print('* '*50)
# 层次化索引的聚合运算
# 旧版写法: df.sum(level=0) - 在pandas 2.0+中已被移除
# 新版写法: 须使用 groupby(level=0).sum() 来实现按层级的聚合操作
print(df.groupby(level=0).sum(),'通过groupby().sum()函数进行level层的运算,示例为将level 0中分别是a和b中所有元素相加聚合运算的结果')

