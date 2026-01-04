#逻辑运算符有and，or，not，用来连接布尔类型的值进行运算
#三个同时出现在一行代码中时，运算顺序是：刮号>not>and>or
# and运算特点：两边运算结果为True时，结果才为True
a = 10
b = 20
c = 30

rs = (a>b) and (a < c)   #False and  False = False 两个都是相同为False
print(rs)
print((a<c) and (a<b))  #True and  True = True   两个都是相同为True
print((a>c) and (a<b))  #False and  True = False    一个为True，一个为Fasle时，结果为False

#or “或”运算特点：两边只要有一个为True，结果就为 True
print((a<c) or (a<b))  #True or  True = True   两个都是相同为True
print((a>c) or (a<b))  #False or  True = True   一个为假，一个为真时结果为True
print((a>c) or (a>b))  #False or  False = False   一个为假，一个为真时结果为False

#not 非运算 取反运算
print(not(a>c))   # not False  =  True
print(not(a<b))   #not True = False

#成员运算符有in和not in：用来判断元素中有什么元素
#示例：
lst=[11,22,33,44,55,66,77,88]
print(99 in lst)    #结果为False，列表中没有’99‘
print(99 not in lst)    #结果为True，’99‘不在列表中