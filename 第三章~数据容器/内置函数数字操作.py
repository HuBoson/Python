#内置函数公共方法有以下几种方式，同时可以对列表，元组，集合，字典，字符等进行操作
lst=[1,2,3,4,5,6,6]  #列表
s1=(12,2,3,4,5)  #元组
# 1.len（）统计容器中的元素个数
print(len(lst))

# 2.del或del(),删除容器

# 3.max(),返回容器中元素的最大值
print(max(lst))

# 4.min(),返回容器中的最小值
print(min(s1))

# 5.range(start,end,step),生成从开始到结束的数字（如：1-10，不包含10），步长为step，供for循环使用

# 6.enumerate(),函数用于将一个可遍历的数据对象组合为一个索引序列，同时列出数据下标，一般用在for循环中
for x,y in enumerate(lst):
    print(f"下标{x}对应元素是{y}")

# 7.all，any(),主要查询所有元素判断数据布尔值都为True和False
print(all([13,'我们','大家']))   #结果为True或False，相当于and
print(any([13,'我们','大家']))   #结果为True或False，相当于or

#8.hash,id,查询内存中的哈希值或ID码：
print(hash('大家'))     #可以得到一个随机的数字哈希值，每次结果不一样。
print(id('大家'))     #可以得到一个固定的ID码的内存地址，每次结果不一样。

# 9.round(x,d):对x进行保留d位小数，如果不设置d，默认为整数，d为负数时就向整数方向四舍五入取整，
print(round(3.1415926,2))  # 最后2是保留小数点后2位，结果是3.14，四舍五入

# 10.sum(iter):对可迭代对象进行求和运算
print('求和：',sum(lst))