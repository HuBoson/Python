from os import rename
import pandas as pd
import numpy as np
# 示例一:
df=pd.DataFrame([80.5,90,58,88],index=['a','b','c','d'],columns=['scores'])
print(df.index[1:3],'获取index元素')
print(df.columns,'获取columns元素')
print(df.sum(),'默认按列求和')
df.rename(columns={'scores':'sor'},inplace=True) # 重命名须用字典,需设定inplace=True(用赋值的方式也可以),否则不会保存在内存,只能临时一次查看一次.
print(df,'修改列名为sor')
print(df.shape,'通过shape查看df维度是4行一列')
# print((df+1)*2,'DataFrame可以和numpy的Ndarray一样执行加减乘除等元素级的向量化运算')
# print(df.astype('int'),'通过astype可以修改数据类型')
# print(del(df['sor'])),'通过del可以删除列或行')
print('* '*50)

df['hours']=(2.1,1.5,1.6,2.2)    # 新增column列,非常常用
df['name']=pd.DataFrame(['Alpha','Beta','Gamma','Theta'],index=['d','b','a','c'])
print(df,'新增hours列和DataFrame列,DataFrame设定的index会按字母索引顺序对应相应的名字')
print('* '*50)

#示例二:
df1=pd.DataFrame(np.random.randn(6,6),columns=['a','b','c','d','e','f'])
df2=pd.DataFrame(np.random.randn(3,3),columns=['a','b','c'])
df3=df1+df2
print(df3,'会自动对齐两个不同数量相加,拼接而成的DataFrame,没有元素相加的地方会用Nan填充')
df3.fillna(0,inplace=True)
print(df3,'通过fillna可以把Nan空值填充为0的元素,inplace=True保存到内存')
print('* '*50)

# 示例三:
d={'PE':pd.Series([10.,20.,30.,40.],index=['Company a','Company b','Company c','Company d']),
   'PB':pd.Series([2.,3.,2.5,4.],index=['Company a','Company b','Company c','Company d']),
   'ROE':pd.Series([0.06,0.1,0.08,0.02],index=['Company a','Company b','Company c','Company d'])}
df4=pd.DataFrame(d)
print(df4)
print(df4[df4.PE<25],'选出PE小于25的股票')   # 也可以用这个格式写:df4[df4['PE']<25],但df4.PE<25的结果是布尔值
print(df4[(df4.PE<25)&(df4.PB<2.5)],'同时满足两个条件的选股')   # 多个条件需要单独用()分开,且需要用"|"或"&"链接,不能用and或or
print(df4[(df4.PE<25)*1+(df4.PB<2.5)*1+(df4.ROE>0.07)*1>=2],'三个满足2个条件的选股')  #用*1的方式判断bool值来选择(不满足*1的结果是0,为False)