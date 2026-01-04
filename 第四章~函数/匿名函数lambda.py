#函数与匿名函数定义功能完全一致，但两个区别如下：
#普通函数需要用def关键字来定义带有名称的函数，可以重复使用。
#lambda关键字匿名函数是定义一个无名称的函数，只可以临时使用一次，且只能有一行代码，无法多行
#匿名函数代码比普通函数更简洁高效
#语法表达：变量=lambda参数x：y（返回值），y(根据需要设定的表达式)就是对冒号前面x(可以是多个参数）做何种的操作，得到的一个返回值返回给前面的变量
# lambda是一个函数，不是实际参数，需要接受的变量去传入实际的参数进行调用
# 作为参数传递给高阶函数，注意配合map()（对元素应用操作）、filter()（过滤元素）、sorted()（自定义排序规则）进行使用
# 变量名=apply(lambda x:y,z)，变量名=sorted(lambda x:y,z)，变量名=filter(lambda x:y,z)，z为需要操作的元素
# 在数据处理、事件回调或闭包中快速定义简单逻辑
#示例：
def test(fun):
    rs=fun(3,4,5)    #变量=lambda参数1，参数2.. ：返回值
    print(rs)
test(lambda a,b,c: a+b+c)   # lambda省去了return关键字，直接接收返回值，只能有一行代码
test(lambda a,b,c: a*b*c)   # lambda作为参数临时调用

print('-'*40)
# 使用lambda进行列表取值操作
lst=[10,20,30,40,50]
for i in range(len(lst)):
    rs=lambda x:x[i]  #根据索引取值，x是形式参数
    print(rs(lst))   #lst是实际参数

print('-'*40)
# 使用lambda进行列表排序操作
stu=[{'name':'陈梅梅','sore':98},
     {'name':'王一一','sore':95},
     {'name':'张天乐','sore':100},
     {'name':'白雪儿','sore':65}]
stu.sort(key=lambda x:x.get('sore'),reverse=True)  #sort排序，使用key做排序，x字典，get去除x字典中的sore数字，reverse反向取值（正向的数字是从小到大）
print(stu)   # 结果按sore；100数字大小往下排序
