import numpy as np
import pandas as pd
import seaborn as sns
"""
concat:简单直接拼接, axis=0(默认)直接将两个表格上下纵向拼接,不去重,axis=1横向拼接,会自动去重,且自动匹配index索引,和join(outer)实现的效果一样
join: 语法结构不同拼接的(df分别在join左右结构),且无需引入pd.,列名称相同的表格时,需要将其中一个列名增加后缀,如: _r, 否则程序报错.
      根据两张表格的index索引拼接,默认在左表格,可以设定交集(双方都有的才保留),并集的拼接(全部保留).
merge: 功能全面,且常用方法,可以按列和索引进行拼接(常用按列,concat和join只能按索引index拼接)
      同等数量的列合并: 需要有同名,同数量,同元素的相同列,默认会根据同名列合并,但索引index会重置从0开始,合并列有元素不同时,合并后只会保留有相同元素的行.
      非同等数量的列合并:合并两个没有列名相同的表格,可以设定left_on和right_on左右各表格以那个列进行合并.设定how=outer并集或交集,保留所有元素,用Nan填充空值
使用DataFrame进行拼接: 使用表格对应的两个列进行拼接,与concat横向拼接,join并集拼接三者效果一致,自动去重
"""
df1=pd.DataFrame(['10','20','25','30'],index=['a','b','c','d'],columns=['PE'])
df2=pd.DataFrame(['2.5','3.2','2.5'],index=['a','d','g'],columns=['PB'])
# print(df1,df2)

# concat拼接:
print(pd.concat([df1,df2],axis=0,sort=False),'concat纵向拼接axis=0,不去重')
print("* "*50)
print(pd.concat([df1,df2],axis=1,sort=False),'concat横向拼接axis=1,会自动匹配index索引,将重复的索引合并')
print("* "*50)
print(pd.concat([df1,df2],ignore_index=True),'通过ignore_index函数将index索引设定从0开始')
print("* "*50)

# join拼接:语法结构不同,且无需引入pd.
print(df1.join(df2,how='right'),'默认是以left左边对齐拼接,以右边为准拼接,多余的不保留,此处df2写在join右边')
print("* "*50)
print(df1.join(df2,how='inner'),'inner交集拼接,双方都有的才会保留')
print("* "*50)
print(df1.join(df2,how='outer'),'outer并集拼接,去重且保留双方所有的元素,没有的用Nan空值填充')
print("* "*50)

# 使用DataFrame进行拼接:
df=pd.DataFrame({'PE':df1['PE'],'PB':df2['PB']})
print(df,'使用DataFrame拼接,使用表格对应的两个列进行拼接,与concat横向拼接,join并集拼接三者效果一致,自动去重')
print("* "*50)

# merge拼接(同等数量列合并):
df2=pd.DataFrame(['2.5','3.2','2.5','2'],index=['a','b','c','d'],columns=['PB'])
roe=pd.Series([0.12,0.05,0.08,0.02],index=['a','b','c','d'])
df1['roe']=roe        # df1表格新增加roe列
df2['roe']=roe        # df2表格新增加roe列
print(pd.merge(df1,df2,on='roe'),'默认会根据同名列合并,也可以设定on=列名称同名的列,索引index会重置从0开始')  # 量化常用日期或股票代码为同名列操作
print("* "*50)
print(pd.merge(df1,df2,how='outer',left_index=True,right_index=True),'也可以做到类似join一样按左还是按右的索引拼接,设置how是交集,并集,修改区分同名列的后缀名称')
print("* "*50)
print(df1.join(df2,rsuffix='_r'),'采用join合并列名称相同的表格时,需要将其中一个列名增加后缀,如: _r, 否则程序报错')
print("* "*50)
# merge拼接(非同等数量列合并):
df2=pd.DataFrame(['2.5','3.2','2.5'],index=['a','b','c'],columns=['PB'])
roe=pd.Series([0.12,0.05,0.08],index=['b','d','c'])    # index没有a,合并后默认是Nan空值
df1['roe']=roe        # df1表格增加roe列
df2['roe']=roe        # df1表格增加roe列
print(pd.merge(df1,df2),'默认会根据同名列交集的合并,df1去除了最后一行,roe列有d无a,不保留d,a为Nan空值,也可以设定on=同名列名称,索引index会重置从0开始')
print("* "*50)
print(pd.merge(df1,df2,how="outer"),'设定how=outer并集,保留所有元素,用Nan填充空值')
print("* "*50)
df1['roe_1']=roe        # df1表格增加roe_1列
df2['roe_2']=roe        # df1表格增加roe_2列
print(pd.merge(df1,df2,left_on='roe_1',right_on='roe_2',how='outer'),'合并两个没有列名相同的表格,可以设定left_on和right_on左右各表格以那个列进行合并,设定how=outer并集,保留所有元素,用Nan填充空值')
