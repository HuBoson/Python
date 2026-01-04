"""
time模块仅限于记录代码执行时间,记录事件发生的时间戳,time sleep()方便实现简单的延迟操作,
time用于表示一天中的某个时间点，不包含日期信息
其余时间排序\格式化等操作主要使用datetime模块实现
time模块是python中的标准库，可以用来进行时间处理、时间格式化和计时等
time():获取当前时间戳
localtime(sec):获取指定时间戳对应的本地时间的struct_time对象
ctime():获取当前时间戳对应的易读字符串
strftime():格式化时间，结果为字符串，str为字符串，f为format
strptime():提取字符串的时间，结果为struct_time对象
sleep(sec):休眠sec秒
%time+变量名称：统计该函数的系统运行时间，如："%time a=..."
"""
"""
%Y 年份：0001~9999
%m 月份：01~12
%B 月名：January~December
%d 日期：01-31
%A 星期: Monday~Sunday
%H 小时(24时制)：00-23
%I 小时(12时制)：01-12
%M 分钟：00-59
%S 秒：00-59
"""
import time
now = time.time()    # 获取当前的时间戳
print(now)
print('*'*50)

obj=time.localtime()     # 获取的是struct_time对象，有详细的当前时间日、时、分、周、年等信息
print(obj)
obj2=time.localtime(60)        # 60秒
print(obj2)
print('对应时间是:',obj2.tm_year,obj2.tm_mon,obj2.tm_mday)
print(time.ctime())        # 时间戳用易读字符串表达：Wed Dec  3 12:52:59 2025
print('*'*50)

#日期时间格式化
print(time.strftime("%Y-%m-%d",time.localtime()))   #  2025-12-03
print(time.strftime("%H:%M:%S",time.localtime()))   #  12:56:55
print('%B月份的名称:',time.strftime("%B",time.localtime()))     # December
print('%A星期是:',time.strftime("%A",time.localtime()))     # Wednesday

#字符串转成struct_time
print(time.strptime('2008-08-08','%Y-%m-%d'))   #将易读时间转成struct_time式表达

time.sleep(5)   # 将程序设定停留5秒后再运行后面的程序
print('hello world!')

