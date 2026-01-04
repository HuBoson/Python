import pandas as pd
import numpy as np
"""
pd.timestamp:时间戳(某个具体的时间点),与datetime高度兼容,可通过.to_datetime()数据转换
datetimeindex:pandas下的时间索引格式,有N个timestamp时间戳组成的序列
pd.date_range(start='2018-01-01',end='2018-12-31'):根据datetimeindex,生成指定长度时间日期,也可以单给一个日期,加上时间段参数
pd.period_range:与date_range近似,可以按datetimeindex选取一段时间,也可以按列选取(datetimeindex不能按列),需要一个时间戳,以及一个freq参数
"""
# 示例
dates=['2025-8-1','2025-8-2','2025-12-25']
dates=pd.DatetimeIndex(dates)   # 把字符串的时间格式转换成pandas下的时间索引格式DatetimeIndex(量化数据处理)
df=pd.Series(np.random.randn(3),index=dates)   # 以时间作为index创建的pandas的Series
print(df['2025-8'],'按时间调取8月数据，12月不会显示')
print(df.index[0])   # 按index位置下标调取数据
print(' *'*50)

# to_datetime将字符串列表转换为DatetimeIndex
dates_time=pd.to_datetime(['2025-10-12','2025-12-20','2025-11-25',None])
print(dates_time)
print(' *'*50)

# pd.date_range生成指定长度时间日期,数据类型是DatetimeIndex
dt=pd.date_range(start='2025-01-01',periods=10)
df1=pd.Series(np.random.randn(10),index=dt)
print('使用date_range生成指定长度时间日期的Series列表:',df1)
print(df1['2025-01-01':'2025-01-05'],'根据时间段切片获取数据')              # 获取一个时间段的数据切片
print(df1.loc['2025-01-03'],'根据loc获取的数据')                  # 数据类型本身是DatetimeIndex,可以不用loc,直接获取日期也可以获取,但datefram数据类型不可以
print(' *'*50)

# pd.Period_range生成指定长度时间日期,数据类型是PeriodIndex
dt1=pd.period_range(start='2025-01-01',periods=5,freq='D')   # freq按'D'天生成5个数据
print(dt1+1)  # 也可以向量化在每个日期上增加1日