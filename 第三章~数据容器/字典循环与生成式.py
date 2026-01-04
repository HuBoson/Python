dict={"name":"Tom","age":20,"gender":"男"}

# 1.遍历所有的键值keys()
for key in dict.keys():
    print(key)

# 2.遍历字典所有value值，values()
for value in dict.values():
    print(value)

# 3.遍历字典的元素items()
for item in dict.items():
    print(item)

# 4.遍历字典的键值对，语法将key,value放在for in中两个一起遍历
for key,value in dict.items():   #
    print(f"{key}={value}")     #key=value为一组键值对

#字典生成式：
import random
d={item:random.randint(1,100) for item in range(4) }
print(d)


lst1=[1001,1002,1003]
lst2=["王二","张三","李四"]
d1={key:value for key,value in zip(lst1,lst2)}
print(d1)