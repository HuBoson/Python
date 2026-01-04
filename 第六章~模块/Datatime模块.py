"""
time模块仅限于记录代码执行时间,记录事件发生的时间戳,time sleep()方便实现简单的延迟操作,
其余时间排序\格式化等操作主要使用datetime模块实现
datetime模块可以方便的显示日期，并对日期进行运算
datetime.datetime:表示日期时间的类，可以做日、时、分、秒的运算，不能做年和月的运算
datetime.timedelta:表示时间间隔的类
datetime.date:表示日期的类
datetime.time:表示时间的类
datetime.tzinfo:与时区相关的类
from dateutil.parser import parse :采用此模块转换时间非常方便
import pandas as pd : 量化常用的时间模块

"""
import datetime
from datetime import datetime  # 这个模块里面的模块常用,就会单独再导入,方便后面使用
# datetime:表示日期时间的类
from datetime import datetime   # 从datetime模块中还有一个子的datetime，导入datetime类
dt = datetime.now()
print('当前系统时间为：',dt)
# datetime是一个类，手动创建这个类的对象
dt2=datetime(2028,8,8,20,8)
print('dt2的数据类型',type(dt2),'dt2所表示的日期和时间:',dt2)
# 比较两个datetime类型对象的大小
day1=datetime(2028,8,8,20,8)
day2=datetime(2029,9,9,20,9)
print('比较哪个时间更早',day1<day2)    # True
print('_'*50)

# strftime:将datetime类型与字符串进行转换
nowdt=datetime.now()
str=nowdt.strftime('%Y/%m/%d %H:%M:%S')
print('nowdt的数据类型:',type(nowdt),'数据是:',nowdt)
print('str的数据类型:',type(str),'数据是:',str)
print('_'*50)

# 将字符串类型转成datetime类型
str2='2028年8月8日20点8分'
dt3=datetime.strptime(str2,'%Y年%m月%d日%H点%M分')   # 方法一:使用strptime转换
print('str的数据类型:',type(str),'str数据:',str2)
print('dt3数据类型:',type(dt3),'dt3数据:')
print('_'*50)
from dateutil.parser import parse  #  # 方法二:使用dateutil.parser模块转换,比较智能识别月和日的转换
str3='01-06-2025'
dt4=parse(str3)        # 可以在括号里增加 dayfirst=True确保第一个数字是日期
print(dt4,'dt4的数据类型是:',type(dt4))
import pandas as pd     # 方法三:使用pandas模块转换,量化常用方法
str4=pd.Series(['2025-08-01','2024-09-12','2023-12-30'],name='Course_time') # 是dtype: object数据类型,需转换datetime
dt5=pd.to_datetime(str4)  # 转换datetime
print(dt5)

print('_'*50)
# 可以做日、时、分、秒的运算：
from datetime import timedelta  # 模块导入
# 两个时间运算：
delta1=datetime(2028,10,1)-datetime(2028,5,1)
print('delta1的数据是:',type(delta1),'delta1数据是:',delta1)
print('2028年5月1日之后的1天是:',datetime(2028,5,1)+delta1)

print('_'*50)
# timedelta:通过传入参数的方式创建timedelta对象，不能做年和月的运算，只能做日、时、分、秒的运算
td1=timedelta(10,11)
print('创建一个10天的timedelta对象',td1)
