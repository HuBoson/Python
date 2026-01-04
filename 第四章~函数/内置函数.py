
"""
zip():在处理多个序列（如列表、元组等）时。zip 函数可以将多个可迭代对象“压缩”在一起，
生成一个由元组组成的迭代器，其中每个元组包含来自各个可迭代对象的对应元素。注意：合并时是以最短数据的长度进行合并成新的元组
sorted()：排序,通常搭配lambda使用，reverse=True反转排序
filter(): 筛选，需要从一个序列中筛选出满足特定条件的元素时。filter函数会将指定的函数应用于给定可迭代对象的所有元素，
         并返回一个包含所有使该函数返回 True 的元素的迭代器。同时会去除未筛选到的元素
map(): 数据转换，映射遍历出每个数据进行处理(比for速度快)，对列表每个元素进行数学运算（如平方、求绝对值等），常用于数据类型转换（map(int, str_list)）、
字符串清洗（map(str.strip, text_list)）、数学运算等场景,常搭配lambda使用
语法:map(f(x)+遍历迭代目标对象),对目标对象依次执行f(x)函数,结果为一个迭代器,需转换list使用
reduce()：数据聚合：把传入的函数作用在一个序列上，函数必须接收两个参数，reduce会把上次计算的结果继续和序列的下一个元素做累积计算
对序列求和、求积等累积计算，将字符串转换为整数的聚合操作，实现数据的归约统计功能
使用时需要导入from functools import reduce
语法格式：reduce(function, sequence[, initial]) -> value,与map的区别在于:map是对目标对象单个迭代,reduce是累积迭代计算
"""
import keyword    #系统导入，保留字严格区分大小写
print(keyword.kwlist) #获取py中的保留函数['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global','if', 'import',
# 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',  'with', 'yield']

# zip（）示例：合并时是以最短数据的长度进行合并成新的元组,一般使用时需要转成字典类型
lst1=["赵本山","范伟","苏有朋"]          #人名
lst2=[40,38,35]                       #年龄
lst3=["卖拐","耳朵有福","倚天屠龙记"]     #作品
rs=zip(lst1,lst2,lst3)
for item in rs:
    print(item)    #结果是将3个列表组成一个由元组组成的迭代器

# sorted()示例：对可迭代对象进行排序
lst=[ {"ID":1,"name":"胡一","age":18,"salary":3000},
      {"ID":2,"name":"张三","age":25,"salary":5000},
      {"ID":3,"name":"王二","age":15,"salary":4000},
      {"ID":4,"name":"李四","age":30,"salary":6000} ]
#1.根据年龄排序：默认从小到大排序，如果要从大到小，需采用reverse=True反向
rs=sorted(lst,key=lambda x:x["age"])
print(rs)    #结果是以age数字从小到大的方式排序

#2.根据收入进行排序，通过使用reverse=True反转排序为从大到小：
rs=sorted(lst,key=lambda x:x["salary"],reverse=True)   # 采用reverse=True反向
print(rs)   #结果是以salary数字从大到小的方式排序

# filter()示例：通过指定条件(默认True)过滤序列并返回一个迭代对象，同时会去除未筛选到的元素,常用与选股
lst4=["张三丰","张无忌","张翠山","灭绝师太","小狐仙"]
f=filter(lambda x:x.startswith("张"),lst4)  #如果去除“张”的内容，就在里面加“not”，如：lambda x:not x.startswith("张"),lst4
print(list(f))      #此处f是一个迭代器，需要把数据用列表list装入

# map()示例：通过函数对可迭代对象进行操作返回一个迭代器对象
lst5=[1,2,3,4,5]
r=map(lambda x:x*2,lst5)   # 将列表每个数*2
print(list(r))      # 此处f是一个迭代器，需要把数据用列表list装入

# eval():去掉字符串左右的引号，也可以将字符串数字转换为数字类型，常与input一起使用，用来获取输入的数值
height=eval(input("请输入您的身高"))
print(height)     #得到的数据类型为int或float，而不是str数据
