"""
生成器使用 yield 语句来产生数据，而不是返回数据。每次调用生成器函数时，返回一个值。
每当函数执行到 yield 语句时，它会暂停执行并返回一个值。下一次调用时，函数会从上次离开的地方继续执行。
生成器非常适合用于生成无限序列、需要高效内存管理或需要大量计算的数据流
生成器(generator):本质是迭代器；可以只取部分想要的数据，如海量数据，用的时候每次只需要一部分数据
创建生成器的两种方案：
一，生成器函数：关键字yield,在执行时并不会执行函数，得到的是生成器
1.可以类似return一样返回数据，但可以持续依次执行（return后面不能有执行数据了）
2.可以分段执行生成器函数中的内容，通过next()可以执行到下一个yield位置
3.只能通过next()才能返回数据，直接取用得到是一个生成器，而不是函数
二，生成器表达式：本质是通过遍历的方式一次将生成器的数据取完，
        语法与推导式一样，(需要取出的数据 for循环+if语句)



"""
# 示例一：生成器函数
# def func():
#     print(111)
#     yield 222
#     print(333)
#     yield 444    # 可以多次使用yield生成器返回参数，return只能一次
# ret=func()
# # print(ret)  # 打印出来的结果是generator 生成器
# print(next(ret))   #只有通过next()得到的才是生成器函数“111”和“222”
# print(next(ret))
# print(next(ret))   #像迭代器一样，超出生成器内的元素再取就会报错！#StopIteration停止取出

# 示例二：
# def order():
#     lst=[]
#     for i in range(1000):
#         lst.append(f"数据{i}")
#         if len(lst)==50:  #每次取50个数据（0-49）
#             yield lst
#             lst=[]   #下一次再取数据放到这个列表中
# gen=order()
# print(next(gen))      #第一次取
# print(next(gen))      #第二次取

# 示例三：生成器表达式
gen = (i ** 2 for i in range(10))

# 一个一个取出数据的方式：
# print(next(gen))
# print(next(gen))
# print(next(gen))
# 一次性全部取出数据
for item in gen:
    print(item)
