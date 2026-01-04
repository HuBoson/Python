# 迭代器主要是能让不同的数据类型可以有统一的遍历功能
# iterable:可迭代的数据类型，如：str,list,tuple,dict,set,open(),但int数字类型是不可迭代数据类型
# iterable（可迭代的数据类型）有迭代器功能，可以把数据进行逐一遍历。
# 获取迭代器的两种语法：
#   1,  iter()        常用方式
#   2,  ._iter_()      特殊方法
# 从迭代器中取出数据：不能超出迭代器里的数据元素和次数，否则StopIteration，报错！
#   1. next()     常用方式
#   2. _next_()   特殊方式
#迭代器特性：
# 1，只能依次取数据，不能重复，取到哪里就停留在哪里，但最多不能超过迭代器里的数据元素和次数
# 2，特别节省内存，惰性机制

#示例：
it=iter("我在深圳")
#只能依次取数据，不能重复，取到哪里就停留在哪里，但最多不能超过迭代器里的数据元素和次数
print(next(it))          #iter()  常用方式
print(it.__next__())      #._iter_()   特殊方法
print(next(it))
print(next(it))
# print(next(it))     #StopIteration，报错！数据取完后就不能再取了

#模拟for循环工作原理：
s="我是数据"
it=iter(s)   #用迭代器取可迭代的数据
while 1:
    try:
        date=it.__next__()
        print(date)    #for循环的循环体
    except StopIteration:
        break
    print(123456)
