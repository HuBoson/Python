#推导式概念：可以将循环和条件判断结合一起写的语法，以更简短的方式代码实现序列创建，
# 可以应用于列表、字典、集合，但不能用于元组（元组是用生成器表达式实现）
#1.列表推导式：
lst1 = [x for x in range(1, 11)]  # 利用for循环创建一个1-10的列表，注意语法表达在for前面还需要一个x
print(lst1)
lst2 = [x for x in range(1, 11) if x % 2 == 0]  # 创建一个%2偶数的列表推导式
print(lst2)

# 2.字典推导式
# 案例：创建一个字典：key是1-5数字，value是这个数字的2次方
dict1 = {x: x ** 2 for x in range(1, 6)}  # x为key，**2次方为value
print(dict1)

# 3.推导式实现将两个列表合并为一个字典
# 案例：
lst1 = ['name', 'age', 'gender']
lst2 = ['Tom', 20, 'man']
dict2 = {lst1[x]: lst2[x] for x in range(0, len(lst2))}  #lst1[x]是key,lst2[x]是value，通过for循环获取x下标在长度0，len（lst2）循环下标对应相应的key
print(dict2)

#4.推导式提取字典中的目标数据
#案例：
counts={'IBM':268,'HP':125,'DELL':201,"Lenovo":199,'acer':99}
#提取上述电脑数量大于200的字典数据
dict3={key:value for key,value in counts.items() if value>=200}
print(dict3)

#5.集合推导式
#案例：将列表中的数据以2次方放入集合中：
list1=[1,1,2]
set1={i**2 for i in list1}
print(set1)