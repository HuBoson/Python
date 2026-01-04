#字典常见操作：
# stu = {"zs":20,"lisi":21,"小张":25,"小李":22}
#
# #1.新增元素： 语法为：字典序列[key] = 值，如下操作：
# stu["小明"] =25  #在stu字典添加“小明”25岁，
# print(stu)     #结果会增加一个小明的字典
#
# #2.修改元素： 语法为：字典序列[key] = 值
# stu["小李"]=26
# print(stu)
#
# #3.查询元素：
# #3.1 通过key值查询
# print(stu["小李"])  #如果当前查询的key存在，则打印对应的value值，如果查询key不存在，就会报错！
# #3.2 通过get()查询，语法为：字典序列.get(key,默认值)
# age=stu.get("小陈",23)   #注意：如果当前查找的key不存在，则接收第二个设定值（23），如果不设定第二个参数，不存在就为none
# print(age)
# #3.3 获取所有的key()
# name=stu.keys()    #查询所有人的名字
# print(name)
# print(type(name))  #结果为字典类型
# #3.4 获取所有的value()
# age=stu.values()    #查询所有学生的年龄
# print(age)
# #3.5 获取所有键值组合items()
# x =stu.items()
# print(x)
#
# #4.删除字典或指定的键值对
# #4.1 写法一：del
# # del stu["zs"]
# #4.2 写法二：del()
# del(stu["zs"])
# print(stu)
#
# #5.清空字典 celar()
# stu.clear()
# print(stu)    #结果为空字典{}
#
# #6.字典合并：采用“|”符号将两个字典合并：
# d1={"a":10,"b":20,"c":30}
# d2={"胡":"cc","王":"bb","李":"aa"}
# d3=d1|d2
# print(d3)
from cryptography.hazmat.asn1.asn1 import sequence

# 7.get获取字典里面的某个元素,如果没有该元素,可以设定想要的返回值,程序不会报错,量化常用方法
d4={"a":10,"b":20,"c":30}
print(d4.get('e'))   # 字典中没有e,会返回None

# 8.fromkeys()用于创建一个新字典,以序列seq中元素做字典的键,value为字典所有键对应的初始值
# 使用不可变类型作为初始值
keys = ['key1', 'key2', 'key3']
immutable_value = "default"
new_dict = dict.fromkeys(keys, immutable_value)
print(new_dict)

# 9.update()用于将另一个字典或可迭代的键值对更新到当前字典中。这个方法非常有用，特别是在合并大量字典或更新现有字典的内容时。
# 键冲突: 如果要更新的字典或可迭代对象中包含与原始字典相同的键，则这些键的值会被覆盖。
# 性能: 对于大型字典，update() 方法通常比手动逐个插入键值对更高效。
original_dict = {'x': 10, 'y': 20}
# 包含键值对的可迭代对象
iterable_pairs = [('x', 15), ('z', 30)]
# 更新原始字典
original_dict.update(iterable_pairs)
print(original_dict)  # 输出: {'x': 15, 'y': 20, 'z': 30}