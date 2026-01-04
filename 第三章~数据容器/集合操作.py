#集合常用操作有以下几种：
set={1,2,3,2,5}

#1.add(),往集合内增加一个元素
set.add(4)  #往set1集合内添加“4”
print(set)  #打印结果会增加“4”

#2.remove(),移除集合内指定的元素
set.remove(2)  #删除集合中的“2“
print(set)

# 3.pop(),从集合中随机取出一个元素
num=set.pop()
print(f"得到的随机元素是{num}")

#4.len(),得到一个整数的元素数量总和
print(len(set))  #得到的Len数量总和也会去重后的整数

#5.clear(),将集合清空
set.clear()
print(set)  #结果为清除整个集合

s1={11,33,44,55}
s2={10,33,4,66}
#6.交集：intersection或“&”
print(s1.intersection (s2))    # 用这个写法 print(s1&s2) 一样，交集出两个集合相同的元素，不相同的去除
#7.并集：union或“|”
print(s1.union(s2))           # 用这个写法 print(s1|s2) 一样，保留一个重复的元素后，将两个集合的元素合并在一起
#7.差集：union或“-”
print(s1.difference(s2))      # 用这个写法 print(s1-s2) 一样，将s1集合中去除与s2相同的元素
#8. 补集：
print(s1^s2)                 #  去除重复的元素后，将两个集合的元素合并在一起

