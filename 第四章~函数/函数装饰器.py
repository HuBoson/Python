"""
装饰器：本质上是一个闭包函数
作用:在不改变原有函数定义和调用方式的前提下，通过在包装函数 inner中,在调用原函数 fn(*args, **kwargs) 
  的前后插入新代码，从而给原函数增加额外功能,ret 只是用来接收原函数的返回值。
通用装饰语法结构如下：
def wrapper(fn):     # wrapper 是装饰器函数,fn 是被装饰的目标函数
    def inner(*args, **kwargs):   # *args, **kwargs: 接收任意位置参数和关键字参数
        # 1. 目标函数执行前要做的事
        ret = fn(*args, **kwargs)     # 2. 调用目标函数，把参数原样转进去
        # 3. 目标函数执行后要做的事
        return ret
    return inner     # 注意：返回的是函数 inner 本身，不是 inner()
@wrapper     #装饰到一个新的函数中去,相当于new=wrapper(new),将两个函数变量赋值
def new():
    pass
ret = new()

一个函数可以被多个装饰器装饰：
@wrapper1
@wrapper2
def target():
    print('执行目标‘）
    pass
    规则执行顺序: wrapper1 wrapper2 taeget wrapper2 wrapper1
"""


# 添加基础信息示例一：
def xx(a):
    def inner(*args, **kwargs):
        print('基础信息。。。。')
        # 下面装饰器new 的代码执行，即调用新函数new
        ret = a(*args, **kwargs)     # 中间执行真正的函数 a,也是ret
        # 装饰器new2 的代码执行，即调用新函数new2
        print('所有信息包含。。。')     # 最后执行
        return ret
    return inner

@xx     # 相当于 new = xx(new)
def new(user, password):   # 被装饰器转入中间执行的函数
    print('1添加新项目信息为。。。', user, password)
    return "新增员工~~~"

@xx
def new2(VIP等级):
    print('添加新内容,新元素。。。', VIP等级)

ret = new('张三', '123456')    # 实际调用的是 xx 里返回的 inner()
print(ret)
new2('VIP等级:2')
# 原来你直接写 new('张三','123456')
# 加了 @xx 之后，调用方式不变，还是写 new('张三','123456')
# 但实际执行时，已经变成：先执行 xx 里的“前后代码”，中间再执行原来的 new


print('*'*50)

#多个装饰器示例二：
def wrapper1(fn):            #这里的fn = wrapper2.inner
    def inner(*args, **kwargs):
        print('这里是wrapper1, 进入')    #第1个被执行的代码
        ret=fn(*args, **kwargs)       # 返回值是 wrapper2.inner
        print('这里是wrapper1,出去')    #第5个被执行的代码
        return ret
    return inner
def wrapper2(fn):            #这里的fn = target
    def inner(*args, **kwargs):
        print('这里是wrapper2, 进入')    #第2个被执行的代码
        ret=fn(*args, **kwargs)       # 返回值是 target
        print('这里是wrapper2,出去')    #第4个被执行的代码
        return ret
    return inner
@wrapper1    #target=wrapper1(wrapper2.inner) => target:wrapper1.inner
@wrapper2    #target=wrapper2(target) => target:wrapper2.inner
def target():
    print('被装饰器转入中间执行的代码')    # 第3个被执行的代码
target()
#  规则执行顺序: wrapper1 wrapper2 taeget wrapper2 wrapper1